"""
Style Analyzer Module
This module checks for style consistency in writing content.
"""

import os
import re
from collections import Counter

class StyleAnalyzer:
    """Analyzes writing style consistency."""
    
    def __init__(self, workspace_root):
        """Initialize the style analyzer.
        
        Args:
            workspace_root: The root directory of the author workspace
        """
        self.workspace_root = workspace_root
        self.style_guide = {}
        self.vocabulary = {}
        self.author_profile = {}
        self.load_style_data()
    
    # Simple tokenizers to replace NLTK
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
    
    def load_style_data(self):
        """Load style data from the workspace."""
        # Load style guide
        self._load_style_guide()
        # Load vocabulary preferences
        self._load_vocabulary()
        # Load author profile
        self._load_author_profile()
    
    def _load_style_guide(self):
        """Load style guide from .cursor/Author/style_guide.md."""
        style_guide_path = os.path.join(self.workspace_root, '.cursor', 'Author', 'style_guide.md')
        if os.path.exists(style_guide_path):
            try:
                with open(style_guide_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.style_guide = self._parse_style_guide(content)
            except Exception as e:
                print(f"Error loading style guide {style_guide_path}: {e}")
    
    def _load_vocabulary(self):
        """Load vocabulary preferences from .cursor/Author/vocabulary.md."""
        vocab_path = os.path.join(self.workspace_root, '.cursor', 'Author', 'vocabulary.md')
        if os.path.exists(vocab_path):
            try:
                with open(vocab_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.vocabulary = self._parse_vocabulary(content)
            except Exception as e:
                print(f"Error loading vocabulary {vocab_path}: {e}")
    
    def _load_author_profile(self):
        """Load author profile from .cursor/Author/profile.md."""
        profile_path = os.path.join(self.workspace_root, '.cursor', 'Author', 'profile.md')
        if os.path.exists(profile_path):
            try:
                with open(profile_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.author_profile = self._parse_profile(content)
            except Exception as e:
                print(f"Error loading author profile {profile_path}: {e}")
    
    def _parse_style_guide(self, content):
        """Parse style guide markdown to extract rules."""
        style_data = {}
        
        # Extract sections and their content
        sections = {}
        current_section = None
        section_content = []
        
        for line in content.split('\n'):
            # Check for heading
            if line.startswith('# '):
                if current_section and section_content:
                    sections[current_section] = '\n'.join(section_content)
                current_section = line[2:].strip()
                section_content = []
            elif line.startswith('## '):
                if current_section and section_content:
                    sections[current_section] = '\n'.join(section_content)
                current_section = line[3:].strip()
                section_content = []
            elif current_section:
                section_content.append(line)
        
        # Add the final section
        if current_section and section_content:
            sections[current_section] = '\n'.join(section_content)
            
        # Process each section into appropriate rules
        for section, content in sections.items():
            if "Point of View" in section:
                style_data['pov'] = self._extract_pov(content)
            elif "Tense" in section:
                style_data['tense'] = self._extract_tense(content)
            elif "Dialogue" in section:
                style_data['dialogue'] = self._extract_dialogue_rules(content)
            else:
                # General rules
                style_data[section.lower().replace(' ', '_')] = content
                
        return style_data
    
    def _extract_pov(self, content):
        """Extract POV preferences from content."""
        pov = "unknown"
        if "first person" in content.lower():
            pov = "first"
        elif "second person" in content.lower():
            pov = "second"
        elif "third person" in content.lower():
            pov = "third"
            
        # Check if limited or omniscient for third person
        if pov == "third":
            if "limited" in content.lower():
                pov = "third limited"
            elif "omniscient" in content.lower():
                pov = "third omniscient"
                
        return pov
    
    def _extract_tense(self, content):
        """Extract tense preferences from content."""
        if "present tense" in content.lower():
            return "present"
        elif "past tense" in content.lower():
            return "past"
        else:
            return "unknown"
    
    def _extract_dialogue_rules(self, content):
        """Extract dialogue formatting rules."""
        rules = {}
        
        if "double quotes" in content.lower():
            rules['quotes'] = 'double'
        elif "single quotes" in content.lower():
            rules['quotes'] = 'single'
            
        if "Oxford comma" in content.lower():
            rules['oxford_comma'] = True
        
        return rules
    
    def _parse_vocabulary(self, content):
        """Parse vocabulary file to extract preferred and avoided terms."""
        vocabulary = {
            'preferred': {},
            'avoided': []
        }
        
        # Look for sections on preferred terms and avoided terms
        sections = {}
        current_section = None
        section_content = []
        
        for line in content.split('\n'):
            # Check for heading
            if line.startswith('# '):
                if current_section and section_content:
                    sections[current_section] = '\n'.join(section_content)
                current_section = line[2:].strip()
                section_content = []
            elif line.startswith('## '):
                if current_section and section_content:
                    sections[current_section] = '\n'.join(section_content)
                current_section = line[3:].strip()
                section_content = []
            elif current_section:
                section_content.append(line)
        
        # Add the final section
        if current_section and section_content:
            sections[current_section] = '\n'.join(section_content)
            
        # Process preferred terms (typically as replacements)
        if 'Preferred Terms' in sections:
            # Look for patterns like "use X instead of Y"
            for line in sections['Preferred Terms'].split('\n'):
                if line.strip() and 'instead of' in line:
                    parts = line.split('instead of')
                    if len(parts) == 2:
                        preferred = parts[0].strip().strip('use ').strip()
                        avoided = parts[1].strip()
                        vocabulary['preferred'][avoided] = preferred
        
        # Process avoided terms (simple list)
        if 'Avoided Terms' in sections:
            for line in sections['Avoided Terms'].split('\n'):
                term = line.strip('- ').strip()
                if term:
                    vocabulary['avoided'].append(term)
                    
        return vocabulary
    
    def _parse_profile(self, content):
        """Parse author profile to extract style preferences."""
        # Similar implementation to _parse_style_guide
        sections = {}
        current_section = None
        section_content = []
        
        for line in content.split('\n'):
            # Check for heading
            if line.startswith('# '):
                if current_section and section_content:
                    sections[current_section] = '\n'.join(section_content)
                current_section = line[2:].strip()
                section_content = []
            elif line.startswith('## '):
                if current_section and section_content:
                    sections[current_section] = '\n'.join(section_content)
                current_section = line[3:].strip()
                section_content = []
            elif current_section:
                section_content.append(line)
        
        # Add the final section
        if current_section and section_content:
            sections[current_section] = '\n'.join(section_content)
            
        return sections
    
    def analyze_content(self, content, file_path):
        """Analyze content for style consistency issues.
        
        Args:
            content: The text content to analyze
            file_path: The path to the file being analyzed
            
        Returns:
            A list of style issues found in the content
        """
        issues = []
        
        # Check POV consistency
        pov_issues = self._check_pov_consistency(content, file_path)
        issues.extend(pov_issues)
        
        # Check tense consistency
        tense_issues = self._check_tense_consistency(content, file_path)
        issues.extend(tense_issues)
        
        # Check vocabulary usage
        vocab_issues = self._check_vocabulary_usage(content, file_path)
        issues.extend(vocab_issues)
        
        # Check sentence structure
        structure_issues = self._check_sentence_structure(content, file_path)
        issues.extend(structure_issues)
        
        return issues
    
    def _check_pov_consistency(self, content, file_path):
        """Check for point of view consistency."""
        issues = []
        expected_pov = self.style_guide.get('pov', None)
        
        if not expected_pov or expected_pov == "unknown":
            return issues
            
        # Use our simple tokenizer instead of NLTK
        sentences = self._sent_tokenize(content)
        
        # First person indicators
        first_person = ['I', 'me', 'my', 'mine', 'we', 'us', 'our', 'ours']
        # Second person indicators
        second_person = ['you', 'your', 'yours']
        # Third person indicators not exhaustive but common
        third_person = ['he', 'him', 'his', 'she', 'her', 'hers', 'they', 'them', 'their', 'theirs']
        
        for sentence in sentences:
            # Use our simple tokenizer instead of NLTK
            words = self._word_tokenize(sentence.lower())
            
            # Skip dialogue (simplified check)
            if '"' in sentence or "'" in sentence:
                continue
                
            # Check for POV mismatches
            if expected_pov.startswith("first"):
                for word in second_person + third_person:
                    if word in words and not self._is_in_dialogue(sentence, word):
                        issues.append({
                            'type': 'style',
                            'severity': 'warning',
                            'message': f"POV inconsistency: Found '{word}' in content using first person POV",
                            'file': file_path,
                            'line': None
                        })
                        break
                        
            elif expected_pov.startswith("third"):
                for word in first_person + second_person:
                    if word in words and not self._is_in_dialogue(sentence, word):
                        issues.append({
                            'type': 'style',
                            'severity': 'warning',
                            'message': f"POV inconsistency: Found '{word}' in content using third person POV",
                            'file': file_path,
                            'line': None
                        })
                        break
        
        return issues
    
    def _is_in_dialogue(self, sentence, word):
        """Check if a word appears within dialogue quotes."""
        # Very simplified dialogue detection
        in_quotes = False
        words = sentence.split()
        
        for w in words:
            if '"' in w or "'" in w:
                in_quotes = not in_quotes
            if word.lower() in w.lower() and in_quotes:
                return True
                
        return False
    
    def _check_tense_consistency(self, content, file_path):
        """Check for tense consistency."""
        issues = []
        expected_tense = self.style_guide.get('tense', None)
        
        if not expected_tense or expected_tense == "unknown":
            return issues
            
        # This is a simplified implementation
        # A full implementation would use NLP for more accurate tense detection
        past_tense_verbs = ['was', 'were', 'had', 'did', 'said', 'went', 'saw', 'thought']
        present_tense_verbs = ['is', 'are', 'have', 'do', 'say', 'go', 'see', 'think']
        
        # Use our simple tokenizer instead of NLTK
        sentences = self._sent_tokenize(content)
        
        for sentence in sentences:
            # Use our simple tokenizer instead of NLTK
            words = self._word_tokenize(sentence.lower())
            
            # Skip dialogue
            if '"' in sentence or "'" in sentence:
                continue
                
            # Check for tense mismatches
            if expected_tense == "past":
                for verb in present_tense_verbs:
                    if verb in words:
                        issues.append({
                            'type': 'style',
                            'severity': 'warning',
                            'message': f"Tense inconsistency: Found present tense verb '{verb}' in past tense narrative",
                            'file': file_path,
                            'line': None
                        })
                        break
                        
            elif expected_tense == "present":
                for verb in past_tense_verbs:
                    if verb in words:
                        issues.append({
                            'type': 'style',
                            'severity': 'warning',
                            'message': f"Tense inconsistency: Found past tense verb '{verb}' in present tense narrative",
                            'file': file_path,
                            'line': None
                        })
                        break
        
        return issues
    
    def _check_vocabulary_usage(self, content, file_path):
        """Check for vocabulary consistency and preferences."""
        issues = []
        
        # Check for avoided terms
        avoided_terms = self.vocabulary.get('avoided', [])
        for term in avoided_terms:
            if term.lower() in content.lower():
                issues.append({
                    'type': 'style',
                    'severity': 'info',
                    'message': f"Avoided term used: '{term}' is in the author's list of terms to avoid",
                    'file': file_path,
                    'line': None
                })
        
        # Check for preferred term replacements
        preferred_terms = self.vocabulary.get('preferred', {})
        for avoided, preferred in preferred_terms.items():
            if avoided.lower() in content.lower():
                issues.append({
                    'type': 'style',
                    'severity': 'info',
                    'message': f"Consider using '{preferred}' instead of '{avoided}'",
                    'file': file_path,
                    'line': None
                })
        
        return issues
    
    def _check_sentence_structure(self, content, file_path):
        """Check for sentence structure issues and patterns."""
        issues = []
        # Use our simple tokenizer instead of NLTK
        sentences = self._sent_tokenize(content)
        
        # Calculate average sentence length
        sentence_lengths = [len(sentence.split()) for sentence in sentences]
        if sentence_lengths:
            avg_length = sum(sentence_lengths) / len(sentence_lengths)
            
            # Flag very long sentences
            for i, length in enumerate(sentence_lengths):
                if length > 35:  # Arbitrary threshold
                    issues.append({
                        'type': 'style',
                        'severity': 'info',
                        'message': f"Long sentence detected ({length} words). Consider breaking it up for readability.",
                        'file': file_path,
                        'line': None,
                        'details': {
                            'sentence': sentences[i][:100] + '...' if len(sentences[i]) > 100 else sentences[i]
                        }
                    })
            
            # Check for repetitive sentence starts
            sentence_starts = []
            for sentence in sentences:
                words = sentence.split()
                if words:
                    sentence_starts.append(words[0].lower())
            
            start_counter = Counter(sentence_starts)
            for word, count in start_counter.items():
                if count > 3 and len(sentences) > 5:  # Arbitrary threshold
                    issues.append({
                        'type': 'style',
                        'severity': 'info',
                        'message': f"Repetitive sentence beginnings: '{word}' starts {count} sentences",
                        'file': file_path,
                        'line': None
                    })
        
        return issues

    def scan_document(self, document_path):
        """Analyze a single document for style consistency.
        
        Args:
            document_path: Path to the document to analyze
            
        Returns:
            A list of style issues found in the document
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
        """Scan the entire workspace for style consistency issues.
        
        Returns:
            A list of style issues found in the workspace
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