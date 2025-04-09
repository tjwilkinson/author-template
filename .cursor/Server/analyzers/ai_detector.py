"""
AI Detector Module
This module provides more advanced detection of AI-generated content.
"""

import os
import re
import math
from collections import Counter

class AIDetectorAnalyzer:
    """Analyzes text for signs of AI generation."""
    
    def __init__(self, workspace_root):
        """Initialize the AI detector.
        
        Args:
            workspace_root: The root directory of the author workspace
        """
        self.workspace_root = workspace_root
        
        # AI detection configuration
        self.ai_phrases = [
            "in conclusion,", 
            "to summarize,", 
            "as an AI language model", 
            "as we can see,",
            "it's important to note that",
            "it is worth mentioning",
            "it should be noted",
            "this article will explore",
            "in this essay, we will",
            "lastly, it is important to",
            "on the other hand,",
            "moreover, it is essential"
        ]
        
        # Thresholds for detection
        self.repetition_threshold = 0.7  # Threshold for repetitive patterns
        self.burstiness_threshold = 0.5  # Threshold for burstiness score
        self.perplexity_threshold = 70.0  # Threshold for perplexity
    
    def _sent_tokenize(self, text):
        """Simple sentence tokenizer."""
        # Split by common sentence terminators
        sentences = re.split(r'(?<=[.!?])\s+', text)
        # Remove empty sentences
        return [s for s in sentences if s.strip()]
    
    def _word_tokenize(self, text):
        """Simple word tokenizer."""
        # Remove punctuation and split by whitespace
        text = re.sub(r'[^\w\s]', ' ', text.lower())
        return text.split()
    
    def analyze_content(self, content, file_path):
        """Analyze content for AI generation markers.
        
        Args:
            content: The text content to analyze
            file_path: The path to the file being analyzed
            
        Returns:
            A list of AI detection issues found in the content
        """
        issues = []
        
        # Skip very short content
        if len(content) < 200:
            return issues
        
        # Check for AI phrases
        phrase_issues = self._check_ai_phrases(content, file_path)
        issues.extend(phrase_issues)
        
        # Check for unnaturally consistent text
        consistency_issues = self._check_text_consistency(content, file_path)
        issues.extend(consistency_issues)
        
        # Check for low burstiness (indication of AI text)
        burstiness_issues = self._check_burstiness(content, file_path)
        issues.extend(burstiness_issues)
        
        # Check for repetitive patterns
        repetition_issues = self._check_repetitive_patterns(content, file_path)
        issues.extend(repetition_issues)
        
        return issues
    
    def _check_ai_phrases(self, content, file_path):
        """Check for common AI-generated phrases."""
        issues = []
        content_lower = content.lower()
        
        # Count the number of AI phrases found
        found_phrases = []
        for phrase in self.ai_phrases:
            if phrase in content_lower:
                found_phrases.append(phrase)
        
        # If more than one AI phrase is found, it's more likely to be AI content
        if len(found_phrases) >= 2:
            phrases_str = '", "'.join(found_phrases[:3])  # List first 3 phrases at most
            issues.append({
                'type': 'ai_content',
                'severity': 'warning',
                'message': f'Multiple AI-typical phrases detected: "{phrases_str}"',
                'file': file_path,
                'line': None
            })
        elif len(found_phrases) == 1:
            issues.append({
                'type': 'ai_content',
                'severity': 'info',
                'message': f'Potential AI phrase detected: "{found_phrases[0]}"',
                'file': file_path,
                'line': None
            })
        
        return issues
    
    def _check_text_consistency(self, content, file_path):
        """Check for unnaturally consistent text patterns."""
        issues = []
        
        # Tokenize content
        sentences = self._sent_tokenize(content)
        
        # Skip if too few sentences
        if len(sentences) < 10:
            return issues
        
        # Measure sentence length consistency
        sentence_lengths = [len(sentence.split()) for sentence in sentences]
        avg_length = sum(sentence_lengths) / len(sentence_lengths)
        std_dev = math.sqrt(sum((x - avg_length) ** 2 for x in sentence_lengths) / len(sentence_lengths))
        
        # AI text often has unnaturally consistent sentence lengths
        # Human text typically has more variation (higher standard deviation)
        variation_coefficient = std_dev / avg_length if avg_length > 0 else 0
        
        if variation_coefficient < 0.4 and len(sentences) > 15:
            issues.append({
                'type': 'ai_content',
                'severity': 'warning',
                'message': 'Unusually consistent sentence lengths suggest AI-generated content',
                'file': file_path,
                'line': None,
                'details': {
                    'variation_coefficient': round(variation_coefficient, 2),
                    'avg_sentence_length': round(avg_length, 2),
                    'sentence_count': len(sentences)
                }
            })
        
        return issues
    
    def _check_burstiness(self, content, file_path):
        """Check text burstiness - human writing tends to be more bursty than AI content.
        
        Burstiness is a measure of variance in information density across a text.
        Human writing tends to alternate between high-information and low-information sections,
        while AI text tends to maintain a more consistent information density.
        """
        issues = []
        
        # Simple burstiness measure: variance in paragraph lengths
        paragraphs = content.split('\n\n')
        
        # Skip if too few paragraphs
        if len(paragraphs) < 5:
            return issues
        
        paragraph_lengths = [len(para.split()) for para in paragraphs if para.strip()]
        
        # Calculate paragraph length variance
        if not paragraph_lengths:
            return issues
            
        avg_para_length = sum(paragraph_lengths) / len(paragraph_lengths)
        variance = sum((x - avg_para_length) ** 2 for x in paragraph_lengths) / len(paragraph_lengths)
        
        # Normalize by average length to get a burstiness score
        burstiness = math.sqrt(variance) / avg_para_length if avg_para_length > 0 else 0
        
        # Human writing tends to have higher burstiness
        if burstiness < self.burstiness_threshold and len(paragraphs) > 8:
            issues.append({
                'type': 'ai_content',
                'severity': 'info',
                'message': 'Low text burstiness suggests potential AI generation',
                'file': file_path,
                'line': None,
                'details': {
                    'burstiness_score': round(burstiness, 2),
                    'threshold': self.burstiness_threshold,
                    'paragraph_count': len(paragraphs)
                }
            })
        
        return issues
    
    def _check_repetitive_patterns(self, content, file_path):
        """Check for repetitive patterns and structures in text."""
        issues = []
        
        # Check for repetitive sentence structures
        sentences = self._sent_tokenize(content)
        
        # Skip if too few sentences
        if len(sentences) < 10:
            return issues
        
        # Extract sentence starts (first 3 words)
        sentence_starts = []
        for sentence in sentences:
            words = sentence.split()
            if len(words) >= 3:
                start = ' '.join(words[:3]).lower()
                sentence_starts.append(start)
        
        # Count occurrences of each pattern
        start_counter = Counter(sentence_starts)
        
        # Calculate repetition ratio
        total_starts = len(sentence_starts)
        unique_starts = len(start_counter)
        repetition_ratio = 1 - (unique_starts / total_starts) if total_starts > 0 else 0
        
        # High repetition ratio indicates more repeated patterns
        if repetition_ratio > self.repetition_threshold and total_starts > 15:
            # Find the most common patterns
            most_common = start_counter.most_common(3)
            pattern_examples = [f'"{pattern}" ({count} times)' for pattern, count in most_common if count > 1]
            
            if pattern_examples:
                issues.append({
                    'type': 'ai_content',
                    'severity': 'warning',
                    'message': 'Repetitive sentence structures suggest AI-generated content',
                    'file': file_path,
                    'line': None,
                    'details': {
                        'repetition_ratio': round(repetition_ratio, 2),
                        'common_patterns': pattern_examples
                    }
                })
        
        return issues
    
    def scan_document(self, document_path):
        """Analyze a single document for AI content markers.
        
        Args:
            document_path: Path to the document to analyze
            
        Returns:
            A list of AI detection issues found in the document
        """
        issues = []
        
        try:
            with open(document_path, 'r', encoding='utf-8') as f:
                content = f.read()
                rel_path = os.path.relpath(document_path, self.workspace_root)
                issues = self.analyze_content(content, rel_path)
        except Exception as e:
            print(f"Error analyzing document {document_path}: {e}")
            
        return issues
        
    def scan_workspace(self):
        """Scan the entire workspace for AI-generated content.
        
        Returns:
            A list of AI detection issues found in the workspace
        """
        issues = []
        
        # Find all content files
        for root, _, files in os.walk(self.workspace_root):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, self.workspace_root)
                    
                    # Skip files in ignored directories
                    if any(ignored in rel_path for ignored in ['.git', '.cursor/Server']):
                        continue
                        
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            file_issues = self.analyze_content(content, rel_path)
                            issues.extend(file_issues)
                    except Exception as e:
                        print(f"Error reading file {file_path}: {e}")
            
        return issues 