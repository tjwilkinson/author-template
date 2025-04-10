#!/usr/bin/env python3
"""
Author Workspace Server
A server component for monitoring and analyzing writing content.
"""

import os
import sys
import time
import argparse
import yaml
from flask import Flask, render_template, jsonify, request
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pypdfium2 as pdfium
import tempfile
import shutil

# Import all analyzers
from analyzers import PlagiarismAnalyzer, ConsistencyAnalyzer, StyleAnalyzer, AIDetectorAnalyzer

# Create Flask app with proper template directory
app = Flask(__name__, 
           template_folder=os.path.join(os.path.dirname(__file__), 'web', 'templates'))

# Configuration
CONFIG_FILE = os.path.join(os.path.dirname(__file__), 'config.yml')
config = {}
if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, 'r') as f:
        config = yaml.safe_load(f)
else:
    # Default configuration
    config = {
        'workspace_root': os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')),
        'monitoring': {
            'enabled': True,
            'ignore_patterns': ['.git/*', '.cursor/Server/*', '*.pyc', '*.swp'],
            'check_interval': 2.0  # seconds
        },
        'analysis': {
            'consistency_check': True,
            'style_check': True,
            'quality_check': True,
            'originality_check': False,  # Disabled by default as it may require external APIs
            'ai_detection': True  # Enabled by default
        }
    }
    # Create config file
    os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
    with open(CONFIG_FILE, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)

# Global state
analysis_results = {
    'issues': [],
    'stats': {
        'total_files': 0,
        'analyzed_files': 0,
        'issues_found': 0
    },
    'last_updated': None
}

# Global event handler (initialized later)
event_handler = None

class ContentEventHandler(FileSystemEventHandler):
    """Handler for file system events."""
    
    def __init__(self):
        """Initialize the event handler."""
        self.plagiarism_analyzer = PlagiarismAnalyzer(config['workspace_root'])
        self.consistency_analyzer = ConsistencyAnalyzer(config['workspace_root'])
        self.style_analyzer = StyleAnalyzer(config['workspace_root'])
        self.ai_detector_analyzer = AIDetectorAnalyzer(config['workspace_root'])
        self.last_event_time = {}  # To debounce multiple events
        
    def on_modified(self, event):
        """Handle file modification events."""
        if event.is_directory:
            return
            
        if not event.src_path.endswith(('.md', '.txt')):
            return
            
        # Debounce events (some editors trigger multiple save events)
        now = time.time()
        if event.src_path in self.last_event_time and now - self.last_event_time[event.src_path] < 2:
            return
        self.last_event_time[event.src_path] = now
        
        # Analyze the modified file
        self._analyze_file(event.src_path)
            
    def _analyze_file(self, file_path):
        """Analyze a single file for issues."""
        if not os.path.exists(file_path):
            return []
            
        # Skip files in ignored directories
        rel_path = os.path.relpath(file_path, config['workspace_root'])
        if any(ignored in rel_path for ignored in ['.git', '.cursor/Server']):
            return []
            
        # Read file content
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            return []
            
        # Collect issues from various analyzers
        file_issues = []
        
        # Check for style consistency
        if config['analysis']['style_check']:
            style_issues = self.style_analyzer.analyze_content(content, rel_path)
            file_issues.extend(style_issues)
        
        # Check for narrative consistency
        if config['analysis']['consistency_check']:
            consistency_issues = self.consistency_analyzer.analyze_content(content, rel_path)
            file_issues.extend(consistency_issues)
        
        # Check for plagiarism
        if config['analysis']['originality_check']:
            plagiarism_issues = self.plagiarism_analyzer.analyze_content(content, rel_path)
            file_issues.extend(plagiarism_issues)
        
        # Check for AI-generated content
        if config['analysis'].get('ai_detection', False):
            ai_issues = self.ai_detector_analyzer.analyze_content(content, rel_path)
            file_issues.extend(ai_issues)
        
        # Update global analysis results
        if file_issues:
            analysis_results['issues'].extend(file_issues)
            analysis_results['stats']['issues_found'] += len(file_issues)
        analysis_results['stats']['analyzed_files'] += 1
        analysis_results['last_updated'] = time.time()
        
        return file_issues

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status')
def status():
    return jsonify({
        'status': 'running',
        'config': config,
        'analysis_results': analysis_results
    })

@app.route('/api/analyze', methods=['POST'])
def analyze():
    target = request.json.get('target', '')
    target_path = os.path.join(config['workspace_root'], target)
    
    if not os.path.exists(target_path):
        return jsonify({'error': f'Target path not found: {target}'}), 404
    
    if os.path.isfile(target_path):
        # Analyze a single file
        if event_handler is None:
            event_handler = ContentEventHandler()
        issues = event_handler._analyze_file(target_path)
        return jsonify({'success': True, 'issues': issues})
    
    elif os.path.isdir(target_path):
        # Analyze all markdown files in directory
        if event_handler is None:
            event_handler = ContentEventHandler()
        
        all_issues = []
        for root, _, files in os.walk(target_path):
            for file in files:
                if file.endswith(('.md', '.txt')):
                    file_path = os.path.join(root, file)
                    issues = event_handler._analyze_file(file_path)
                    all_issues.extend(issues)
        
        return jsonify({'success': True, 'issues': all_issues})
    
    return jsonify({'error': 'Invalid target'}), 400

@app.route('/api/convert_pdf', methods=['POST'])
def convert_pdf_to_markdown():
    """Convert a PDF file to Markdown."""
    pdf_path = request.json.get('pdf_path', '')
    if not pdf_path:
        return jsonify({'error': 'No PDF path provided'}), 400
    
    # Resolve path
    abs_pdf_path = os.path.join(config['workspace_root'], pdf_path)
    pdf_path_rel = os.path.relpath(abs_pdf_path, config['workspace_root'])
    
    # Check if file exists and is a PDF
    if not os.path.exists(abs_pdf_path):
        return jsonify({'error': f'PDF file not found: {pdf_path_rel}'}), 404
    
    if not abs_pdf_path.lower().endswith('.pdf'):
        return jsonify({'error': f'File is not a PDF: {pdf_path_rel}'}), 400
    
    try:
        # Load PDF document
        pdf_document = pdfium.PdfDocument(abs_pdf_path)
        page_count = len(pdf_document)
        
        # Extract text from each page
        markdown_content = f"# {os.path.basename(abs_pdf_path)}\n\n"
        
        for page_number in range(page_count):
            page = pdf_document[page_number]
            text_page = page.get_textpage()
            page_text = text_page.get_text_range()
            if page_text.strip():
                markdown_content += f"## Page {page_number + 1}\n\n{page_text}\n\n"
        
        # Output file path
        markdown_path = os.path.splitext(abs_pdf_path)[0] + '.md'
        
        # Save to file
        with open(markdown_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        return jsonify({
            'success': True,
            'message': f'PDF converted successfully to {os.path.relpath(markdown_path, config["workspace_root"])}',
            'markdown_path': os.path.relpath(markdown_path, config['workspace_root']),
            'page_count': page_count,
            'markdown_content': markdown_content
        })
    
    except Exception as e:
        error_message = f"Error converting PDF: {str(e)}"
        print(error_message)
        return jsonify({'error': error_message, 'pdf_file': pdf_path_rel}), 500

@app.route('/api/check_plagiarism', methods=['POST'])
def check_plagiarism():
    """Check content for potential plagiarism."""
    content = request.json.get('content', '')
    filepath = request.json.get('filepath', '')
    
    if not content:
        return jsonify({'error': 'No content provided'}), 400
    
    try:
        # Initialize the analyzer if needed
        if event_handler is None:
            event_handler = ContentEventHandler()
        
        # Run the plagiarism check
        issues = event_handler.plagiarism_analyzer.analyze_content(content, filepath)
        
        return jsonify({
            'success': True,
            'issues': issues,
            'analyzed': True
        })
    
    except Exception as e:
        error_message = f"Error checking plagiarism: {str(e)}"
        print(error_message)
        return jsonify({'error': error_message}), 500

@app.route('/api/check_consistency', methods=['POST'])
def check_consistency():
    """Check content for narrative consistency."""
    content = request.json.get('content', '')
    filepath = request.json.get('filepath', '')
    
    if not content:
        return jsonify({'error': 'No content provided'}), 400
    
    try:
        # Initialize the analyzer if needed
        if event_handler is None:
            event_handler = ContentEventHandler()
        
        # Run the consistency check
        issues = event_handler.consistency_analyzer.analyze_content(content, filepath)
        
        return jsonify({
            'success': True,
            'issues': issues,
            'analyzed': True
        })
    except Exception as e:
        error_message = f"Error checking consistency: {str(e)}"
        print(error_message)
        return jsonify({'error': error_message}), 500

@app.route('/api/check_style', methods=['POST'])
def check_style():
    """Check content for style consistency."""
    content = request.json.get('content', '')
    filepath = request.json.get('filepath', '')
    
    if not content:
        return jsonify({'error': 'No content provided'}), 400
    
    try:
        # Initialize the analyzer if needed
        if event_handler is None:
            event_handler = ContentEventHandler()
        
        # Run the style check
        issues = event_handler.style_analyzer.analyze_content(content, filepath)
        
        return jsonify({
            'success': True,
            'issues': issues,
            'analyzed': True
        })
    except Exception as e:
        error_message = f"Error checking style: {str(e)}"
        print(error_message)
        return jsonify({'error': error_message}), 500

@app.route('/api/check_ai_content', methods=['POST'])
def check_ai_content():
    """Check content for indicators of AI-generated text."""
    content = request.json.get('content', '')
    filepath = request.json.get('filepath', '')
    
    if not content:
        return jsonify({'error': 'No content provided'}), 400
    
    try:
        # Initialize the analyzer if needed
        if event_handler is None:
            event_handler = ContentEventHandler()
        
        # Run the AI detection check
        issues = event_handler.ai_detector_analyzer.analyze_content(content, filepath)
        
        return jsonify({
            'success': True,
            'issues': issues,
            'analyzed': True
        })
    except Exception as e:
        error_message = f"Error checking for AI content: {str(e)}"
        print(error_message)
        return jsonify({'error': error_message}), 500

def start_monitoring(workspace_path):
    """Start the file system monitoring."""
    global event_handler
    
    if event_handler is None:
        event_handler = ContentEventHandler()
    
    observer = Observer()
    observer.schedule(event_handler, workspace_path, recursive=True)
    observer.start()
    print(f"Started monitoring {workspace_path}")
    return observer

def main():
    """Main entry point for the server."""
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Author Workspace Server')
    parser.add_argument('--mode', choices=['continuous', 'batch', 'validate'], default='continuous',
                       help='Server operation mode: continuous monitoring, batch analysis, or validation')
    parser.add_argument('--target', help='Target file or directory for batch or validate modes')
    parser.add_argument('--port', type=int, default=5050, help='Port to run the server on')
    args = parser.parse_args()
    
    # Set up workspace path from config
    workspace_path = config['workspace_root']
    
    # Different modes of operation
    if args.mode == 'continuous':
        # Start monitoring
        observer = start_monitoring(workspace_path)
        
        # Start Flask server
        try:
            app.run(host='127.0.0.1', port=args.port, debug=False)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
    
    elif args.mode == 'batch':
        if not args.target:
            print("Error: --target is required for batch mode")
            sys.exit(1)
        
        target_path = os.path.join(workspace_path, args.target)
        if not os.path.exists(target_path):
            print(f"Error: Target path not found: {args.target}")
            sys.exit(1)
        
        # Create handler
        handler = ContentEventHandler()
        
        # Process files
        if os.path.isfile(target_path):
            issues = handler._analyze_file(target_path)
            print(f"Analyzed 1 file, found {len(issues)} issues.")
        else:
            file_count = 0
            all_issues = []
            for root, _, files in os.walk(target_path):
                for file in files:
                    if file.endswith(('.md', '.txt')):
                        file_path = os.path.join(root, file)
                        issues = handler._analyze_file(file_path)
                        all_issues.extend(issues)
                        file_count += 1
            
            print(f"Analyzed {file_count} files, found {len(all_issues)} issues.")
    
    elif args.mode == 'validate':
        if not args.target:
            print("Error: --target is required for validate mode")
            sys.exit(1)
        
        target_path = os.path.join(workspace_path, args.target)
        if not os.path.exists(target_path) or not os.path.isfile(target_path):
            print(f"Error: Target file not found: {args.target}")
            sys.exit(1)
        
        # Create handler and analyze
        handler = ContentEventHandler()
        issues = handler._analyze_file(target_path)
        
        # Output results
        print(f"Validation for {args.target}:")
        print(f"Found {len(issues)} issues.")
        for issue in issues:
            print(f"- {issue['type']} ({issue['severity']}): {issue['message']}")

if __name__ == '__main__':
    main() 