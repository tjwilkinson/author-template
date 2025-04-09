"""
Plagiarism Analyzer Module
This module checks for potential plagiarism and self-plagiarism in writing content.
"""

import os
import re
import difflib
from collections import defaultdict
# Remove NLTK dependency
# from nltk.tokenize import sent_tokenize

class PlagiarismAnalyzer:
    """Analyzes text for potential plagiarism issues."""
    
    def __init__(self, workspace_root):
        """Initialize the plagiarism analyzer.
        
        Args:
            workspace_root: The root directory of the author workspace
        """
        self.workspace_root = workspace_root
        self.content_cache = {}  # Cache of previously analyzed content
        self.fingerprints = defaultdict(list)  # For storing content fingerprints
        self.chunk_size = 5  # Number of sentences to check in a chunk
        self.similarity_threshold = 0.8  # Similarity threshold for flagging
    
    def _sent_tokenize(self, text):
        """Simple sentence tokenizer."""
        # Split by common sentence terminators
        sentences = re.split(r'(?<=[.!?])\s+', text)
        # Remove empty sentences
        return [s for s in sentences if s.strip()]
        
    def analyze_content(self, content, file_path):
        """Analyze content for potential plagiarism.
        
        Args:
            content: The text content to analyze
            file_path: The path to the file being analyzed
            
        Returns:
            A list of potential plagiarism issues found in the content
        """
        issues = []
        rel_path = os.path.relpath(file_path, self.workspace_root)
        
        # Skip if the file is already in our cache (avoid self-matches)
        if rel_path in self.content_cache:
            return issues
        
        # Add to cache
        self.content_cache[rel_path] = content
        
        # Check for self-plagiarism
        self_plagiarism_issues = self._check_self_plagiarism(content, rel_path)
        issues.extend(self_plagiarism_issues)
        
        # Check for AI content (simplified placeholder)
        ai_content_issues = self._check_ai_content(content, rel_path)
        issues.extend(ai_content_issues)
        
        # Generate and store fingerprints for this document
        self._generate_fingerprints(content, rel_path)
        
        return issues
    
    def _check_self_plagiarism(self, content, file_path):
        """Check for self-plagiarism against other documents in the workspace."""
        issues = []
        # Use our custom tokenizer instead of NLTK
        sentences = self._sent_tokenize(content)
        
        # Process text in chunks for more efficient comparison
        for i in range(0, len(sentences), self.chunk_size):
            chunk = ' '.join(sentences[i:i+self.chunk_size])
            
            # Skip very short chunks
            if len(chunk) < 50:
                continue
                
            # Compare against other documents
            for other_path, other_content in self.content_cache.items():
                # Skip comparison with self
                if other_path == file_path:
                    continue
                    
                # Check for substantial similarity
                # Use our custom tokenizer instead of NLTK
                other_sentences = self._sent_tokenize(other_content)
                for j in range(0, len(other_sentences), self.chunk_size):
                    other_chunk = ' '.join(other_sentences[j:j+self.chunk_size])
                    
                    # Skip very short chunks
                    if len(other_chunk) < 50:
                        continue
                        
                    # Calculate similarity
                    similarity = difflib.SequenceMatcher(None, chunk, other_chunk).ratio()
                    
                    if similarity > self.similarity_threshold:
                        issues.append({
                            'type': 'plagiarism',
                            'severity': 'warning',
                            'message': f'Potential self-plagiarism: Similar content found in {other_path}',
                            'file': file_path,
                            'line': None,  # Would compute actual line number in a full implementation
                            'details': {
                                'similarity': similarity,
                                'source': other_path,
                                'matching_text': chunk[:100] + '...' if len(chunk) > 100 else chunk
                            }
                        })
        
        return issues
    
    def _check_ai_content(self, content, file_path):
        """Check for potential AI-generated content.
        
        Note: This is a simplified placeholder. A real implementation would use 
        more sophisticated AI detection techniques or external APIs.
        """
        issues = []
        
        # Simplified AI detection heuristics
        # These are NOT reliable indicators, just examples for the demo
        # Use our custom tokenizer instead of NLTK
        sentences = self._sent_tokenize(content)
        
        # Check for extremely consistent sentence length
        if len(sentences) > 10:
            sentence_lengths = [len(s) for s in sentences]
            avg_length = sum(sentence_lengths) / len(sentence_lengths)
            consistent_count = sum(1 for length in sentence_lengths if abs(length - avg_length) < 20)
            
            if consistent_count / len(sentences) > 0.9:
                issues.append({
                    'type': 'plagiarism',
                    'severity': 'info',
                    'message': 'Unusually consistent sentence lengths - potential AI-generated content',
                    'file': file_path,
                    'line': None
                })
        
        # Check for typical AI phrases
        ai_indicators = [
            "in conclusion,", 
            "to summarize,", 
            "as an AI language model", 
            "as we can see,",
            "it's important to note that"
        ]
        
        for indicator in ai_indicators:
            if indicator in content.lower():
                issues.append({
                    'type': 'plagiarism',
                    'severity': 'info',
                    'message': f'Potential AI-generated content detected: Uses phrase "{indicator}"',
                    'file': file_path,
                    'line': None
                })
                break
        
        return issues
    
    def _generate_fingerprints(self, content, file_path):
        """Generate and store fingerprints for this document for future comparisons."""
        # Use our custom tokenizer instead of NLTK
        sentences = self._sent_tokenize(content)
        
        # Generate fingerprints from 3-sentence windows
        for i in range(len(sentences) - 2):
            window = ' '.join(sentences[i:i+3])
            if len(window) < 30:  # Skip very short windows
                continue
                
            # Simple fingerprint generation (a real implementation would use more sophisticated techniques)
            fingerprint = hash(window)
            self.fingerprints[fingerprint].append((file_path, i))
    
    def scan_workspace(self):
        """Scan the entire workspace for plagiarism issues.
        
        Returns:
            A list of potential plagiarism issues found in the workspace
        """
        issues = []
        
        # Clear existing cache and fingerprints
        self.content_cache = {}
        self.fingerprints = defaultdict(list)
        
        # Find all content files
        for root, _, files in os.walk(self.workspace_root):
            for file in files:
                if file.endswith(('.md', '.txt')):
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, self.workspace_root)
                    
                    # Skip files in ignored directories
                    if any(ignored in rel_path for ignored in ['.git', '.cursor/Server']):
                        continue
                        
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            self.content_cache[rel_path] = content
                    except Exception as e:
                        print(f"Error reading file {file_path}: {e}")
        
        # Compare all files
        for file_path, content in self.content_cache.items():
            file_issues = self.analyze_content(content, os.path.join(self.workspace_root, file_path))
            issues.extend(file_issues)
            
        return issues 