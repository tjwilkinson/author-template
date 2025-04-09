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
            'originality_check': False  # Disabled by default as it may require external APIs
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

class ContentEventHandler(FileSystemEventHandler):
    def __init__(self, analyzers=None):
        self.analyzers = analyzers or []
        self.last_event_time = time.time()
        self.issues = []
        
    def on_modified(self, event):
        if event.is_directory:
            return
            
        # Check file extension - only analyze markdown files
        if not event.src_path.endswith(('.md', '.txt')):
            return
            
        # Check against ignore patterns
        for pattern in config['monitoring']['ignore_patterns']:
            if self._matches_pattern(event.src_path, pattern):
                return
                
        # Debounce events (multiple events can fire for a single save)
        current_time = time.time()
        if current_time - self.last_event_time < 1.0:
            return
        self.last_event_time = current_time
        
        # Analyze the modified file
        self._analyze_file(event.src_path)
        
    def _matches_pattern(self, path, pattern):
        # Simple pattern matching (could be enhanced with proper glob matching)
        if pattern.startswith('*'):
            return path.endswith(pattern[1:])
        elif pattern.endswith('*'):
            return path.startswith(os.path.join(config['workspace_root'], pattern[:-1]))
        else:
            return pattern in path
            
    def _analyze_file(self, file_path):
        print(f"Analyzing file: {file_path}")
        rel_path = os.path.relpath(file_path, config['workspace_root'])
        
        # Read file content
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading file: {e}")
            return
            
        # Run analyzers
        file_issues = []
        
        # Simple consistency check (placeholder for actual NLP analysis)
        if config['analysis']['consistency_check']:
            # This would be replaced with actual NLP-based consistency checking
            if 'character' in content.lower() and not os.path.exists(os.path.join(
                    config['workspace_root'], 'Research', 'Characters')):
                file_issues.append({
                    'type': 'consistency',
                    'severity': 'warning',
                    'message': 'Character mentioned but no character profiles found',
                    'file': rel_path,
                    'line': None  # Would be populated with actual line number
                })
        
        # Simple style check (placeholder)
        if config['analysis']['style_check']:
            # Count number of passive voice instances (very simplified example)
            passive_indicators = ['was made', 'were made', 'is being', 'was being', 'were being']
            for indicator in passive_indicators:
                if indicator in content.lower():
                    file_issues.append({
                        'type': 'style',
                        'severity': 'info',
                        'message': f'Possible passive voice: "{indicator}"',
                        'file': rel_path,
                        'line': None
                    })
        
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
        return jsonify({'error': f'Target not found: {target}'}), 404
        
    # Clear previous results
    analysis_results['issues'] = []
    analysis_results['stats'] = {
        'total_files': 0,
        'analyzed_files': 0,
        'issues_found': 0
    }
    
    # Analyze directory or single file
    if os.path.isdir(target_path):
        for root, _, files in os.walk(target_path):
            for file in files:
                if file.endswith(('.md', '.txt')):
                    file_path = os.path.join(root, file)
                    event_handler._analyze_file(file_path)
                    analysis_results['stats']['total_files'] += 1
    else:
        event_handler._analyze_file(target_path)
        analysis_results['stats']['total_files'] = 1
    
    return jsonify(analysis_results)

@app.route('/api/convert_pdf', methods=['POST'])
def convert_pdf_to_markdown():
    """Convert a specified PDF file to Markdown using pypdfium2."""
    
    pdf_path_rel = request.json.get('pdf_path')
    if not pdf_path_rel:
        return jsonify({'error': 'Missing "pdf_path" in request body'}), 400

    pdf_path_abs = os.path.join(config['workspace_root'], pdf_path_rel)
    if not os.path.exists(pdf_path_abs):
        return jsonify({'error': f'PDF file not found: {pdf_path_rel}'}), 404
    
    if not pdf_path_abs.lower().endswith('.pdf'):
         return jsonify({'error': f'File is not a PDF: {pdf_path_rel}'}), 400

    markdown_content = ""
    error_message = None

    try:
        print(f"Starting conversion for: {pdf_path_rel}")
        
        # Open the PDF
        pdf = pdfium.PdfDocument(pdf_path_abs)
        num_pages = len(pdf)
        
        # Create markdown header
        pdf_filename = os.path.basename(pdf_path_rel)
        markdown_content = f"# {pdf_filename}\n\n"
        
        # Extract text from each page
        for page_num in range(num_pages):
            page = pdf[page_num]
            text_page = page.get_textpage()
            page_text = text_page.get_text_range()
            
            if page_text.strip():
                # Add page header and text
                markdown_content += f"## Page {page_num + 1}\n\n"
                
                # Process text to make it more markdown-friendly
                paragraphs = [p for p in page_text.split('\n\n') if p.strip()]
                for para in paragraphs:
                    # Clean up paragraph text
                    para = para.replace('\n', ' ').strip()
                    if para:
                        markdown_content += f"{para}\n\n"
        
        # Determine the output file path
        output_dir = os.path.dirname(pdf_path_abs)
        base_name = os.path.splitext(os.path.basename(pdf_path_abs))[0]
        markdown_file_path = os.path.join(output_dir, f"{base_name}.md")
        markdown_file_rel = os.path.join(os.path.dirname(pdf_path_rel), f"{base_name}.md")
        
        # Save the markdown content to file
        with open(markdown_file_path, 'w', encoding='utf-8') as md_file:
            md_file.write(markdown_content)
            
        print(f"Conversion complete, saved to: {markdown_file_path}")
        
        # Return success response
        return jsonify({
            'message': 'PDF converted successfully.',
            'pdf_file': pdf_path_rel,
            'markdown_file': markdown_file_rel,
            'num_pages': num_pages
        })

    except Exception as e:
        error_message = f"Error during PDF conversion: {str(e)}"
        app.logger.error(f"PDF conversion error for {pdf_path_rel}: {str(e)}")

    # Return error
    if error_message:
        return jsonify({'error': error_message, 'pdf_file': pdf_path_rel}), 500

def start_monitoring(workspace_path):
    """Start the file system monitoring."""
    global event_handler
    event_handler = ContentEventHandler()
    observer = Observer()
    observer.schedule(event_handler, workspace_path, recursive=True)
    observer.start()
    print(f"Monitoring started for: {workspace_path}")
    return observer


def main():
    """Main entry point for the server."""
    parser = argparse.ArgumentParser(description='Author Workspace Server')
    parser.add_argument('--mode', choices=['continuous', 'batch', 'validate'], 
                        default='continuous', help='Server operation mode')
    parser.add_argument('--target', help='Target file or directory for analysis')
    parser.add_argument('--port', type=int, default=5000, help='Web server port')
    args = parser.parse_args()
    
    workspace_path = config['workspace_root']
    print(f"Author Workspace Server starting...")
    print(f"Workspace root: {workspace_path}")
    
    if args.mode == 'continuous':
        observer = start_monitoring(workspace_path)
        try:
            app.run(debug=True, port=args.port, use_reloader=False)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
    elif args.mode == 'batch' or args.mode == 'validate':
        if not args.target:
            print("Error: --target is required for batch or validate mode")
            sys.exit(1)
        target_path = os.path.join(workspace_path, args.target)
        if not os.path.exists(target_path):
            print(f"Error: Target not found: {target_path}")
            sys.exit(1)
            
        # Create event handler and analyze
        event_handler = ContentEventHandler()
        if os.path.isdir(target_path):
            print(f"Batch analyzing directory: {target_path}")
            for root, _, files in os.walk(target_path):
                for file in files:
                    if file.endswith(('.md', '.txt')):
                        event_handler._analyze_file(os.path.join(root, file))
        else:
            print(f"Analyzing file: {target_path}")
            event_handler._analyze_file(target_path)
            
        # Print results
        print("\nAnalysis Results:")
        print(f"Files analyzed: {analysis_results['stats']['analyzed_files']}")
        print(f"Issues found: {analysis_results['stats']['issues_found']}")
        for issue in analysis_results['issues']:
            print(f"- [{issue['severity']}] {issue['file']}: {issue['message']}")
    
if __name__ == "__main__":
    main() 