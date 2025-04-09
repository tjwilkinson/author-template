"""
Consistency Analyzer Module
This module checks the consistency of narrative elements across writing projects.
"""

import os
import re
# Remove NLTK dependency
# from nltk.tokenize import sent_tokenize, word_tokenize

class ConsistencyAnalyzer:
    """Analyzes consistency of narrative elements."""
    
    def __init__(self, workspace_root):
        """Initialize the consistency analyzer.
        
        Args:
            workspace_root: The root directory of the author workspace
        """
        self.workspace_root = workspace_root
        self.character_profiles = {}
        self.setting_profiles = {}
        self.terminology = {}
        self.load_reference_data()
    
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
    
    def load_reference_data(self):
        """Load reference data from the workspace."""
        # Load character profiles
        self._load_character_profiles()
        # Load setting descriptions
        self._load_setting_profiles()
        # Load terminology
        self._load_terminology()
    
    def _load_character_profiles(self):
        """Load character profiles from Research/Characters and Shared/Characters."""
        # Check for single project structure
        character_dir = os.path.join(self.workspace_root, 'Research', 'Characters')
        if os.path.exists(character_dir):
            self._load_profiles_from_dir(character_dir, self.character_profiles)
        
        # Check for multi-project structure
        shared_char_dir = os.path.join(self.workspace_root, 'Shared', 'Characters')
        if os.path.exists(shared_char_dir):
            self._load_profiles_from_dir(shared_char_dir, self.character_profiles)
            
        # Load from individual projects
        projects_dir = os.path.join(self.workspace_root, 'Projects')
        if os.path.exists(projects_dir):
            for project in os.listdir(projects_dir):
                project_char_dir = os.path.join(projects_dir, project, 'Research', 'Characters')
                if os.path.exists(project_char_dir):
                    self._load_profiles_from_dir(project_char_dir, self.character_profiles)
    
    def _load_setting_profiles(self):
        """Load setting descriptions from Research/Settings and Shared/Settings."""
        # Similar to _load_character_profiles but for settings
        setting_dir = os.path.join(self.workspace_root, 'Research', 'Settings')
        if os.path.exists(setting_dir):
            self._load_profiles_from_dir(setting_dir, self.setting_profiles)
        
        shared_setting_dir = os.path.join(self.workspace_root, 'Shared', 'Settings')
        if os.path.exists(shared_setting_dir):
            self._load_profiles_from_dir(shared_setting_dir, self.setting_profiles)
    
    def _load_terminology(self):
        """Load terminology from Research/Terminology and Shared/Terminology."""
        # Load terminology files
        term_files = []
        
        # Check for single project structure
        term_dir = os.path.join(self.workspace_root, 'Research', 'Terminology')
        if os.path.exists(term_dir):
            term_files.extend([os.path.join(term_dir, f) for f in os.listdir(term_dir) if f.endswith('.md')])
        
        # Check for multi-project structure
        shared_term_dir = os.path.join(self.workspace_root, 'Shared', 'Terminology')
        if os.path.exists(shared_term_dir):
            term_files.extend([os.path.join(shared_term_dir, f) for f in os.listdir(shared_term_dir) if f.endswith('.md')])
        
        # Parse terminology files
        for term_file in term_files:
            self._parse_terminology_file(term_file)
    
    def _load_profiles_from_dir(self, directory, profile_dict):
        """Load profiles from a directory into the provided dictionary."""
        if not os.path.exists(directory):
            return
            
        for filename in os.listdir(directory):
            if not filename.endswith('.md'):
                continue
                
            filepath = os.path.join(directory, filename)
            profile_name = os.path.splitext(filename)[0]
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    profile_dict[profile_name] = self._parse_profile(content)
            except Exception as e:
                print(f"Error loading profile {filepath}: {e}")
    
    def _parse_profile(self, content):
        """Parse a profile markdown file to extract structured data."""
        # A simple parser that extracts headings and content
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
    
    def _parse_terminology_file(self, filepath):
        """Parse a terminology file to extract terms and definitions."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Look for term definitions in formats like:
            # - **Term**: Definition
            # - Term: Definition
            # - # Term
            #   Definition
            
            # Pattern for inline definitions
            inline_pattern = r'\*\*([^*]+)\*\*:\s*([^\n]+)'
            for match in re.finditer(inline_pattern, content):
                term, definition = match.groups()
                self.terminology[term.strip()] = definition.strip()
                
            # Pattern for heading-based definitions
            lines = content.split('\n')
            current_term = None
            term_content = []
            
            for line in lines:
                if line.startswith('# '):
                    if current_term and term_content:
                        self.terminology[current_term] = '\n'.join(term_content)
                    current_term = line[2:].strip()
                    term_content = []
                elif line.startswith('## '):
                    if current_term and term_content:
                        self.terminology[current_term] = '\n'.join(term_content)
                    current_term = line[3:].strip()
                    term_content = []
                elif current_term and line.strip():
                    term_content.append(line)
            
            # Add the final term
            if current_term and term_content:
                self.terminology[current_term] = '\n'.join(term_content)
                
        except Exception as e:
            print(f"Error parsing terminology file {filepath}: {e}")
    
    def analyze_content(self, content, file_path):
        """Analyze content for consistency issues.
        
        Args:
            content: The text content to analyze
            file_path: The path to the file being analyzed
            
        Returns:
            A list of consistency issues found in the content
        """
        issues = []
        
        # Check for character consistency
        character_issues = self._check_character_consistency(content, file_path)
        issues.extend(character_issues)
        
        # Check for setting consistency
        setting_issues = self._check_setting_consistency(content, file_path)
        issues.extend(setting_issues)
        
        # Check for terminology consistency
        term_issues = self._check_terminology_consistency(content, file_path)
        issues.extend(term_issues)
        
        return issues
    
    def _check_character_consistency(self, content, file_path):
        """Check for character consistency issues."""
        issues = []
        # Use our custom tokenizer instead of NLTK
        sentences = self._sent_tokenize(content)
        
        # For each character in our profiles
        for char_name, char_profile in self.character_profiles.items():
            # Check if the character is mentioned in the content
            if char_name.lower() in content.lower():
                # If we have physical description data
                if 'Physical Description' in char_profile:
                    physical_desc = char_profile['Physical Description'].lower()
                    eyes_match = re.search(r'(?:eyes?|eye color)[\s:]+(\w+)', physical_desc)
                    hair_match = re.search(r'(?:hairs?|hair color)[\s:]+(\w+)', physical_desc)
                    
                    # Check for inconsistent eye color
                    if eyes_match:
                        expected_eye_color = eyes_match.group(1)
                        for sentence in sentences:
                            if char_name.lower() in sentence.lower() and 'eye' in sentence.lower():
                                # Check for inconsistent descriptions
                                for color in ['blue', 'green', 'brown', 'hazel', 'gray', 'black']:
                                    if color != expected_eye_color and f"{char_name}'s {color} eyes" in sentence.lower():
                                        issues.append({
                                            'type': 'consistency',
                                            'severity': 'warning',
                                            'message': f"Character '{char_name}' eye color inconsistency. Profile says '{expected_eye_color}', found '{color}'",
                                            'file': file_path,
                                            'line': None  # Would compute actual line number in a full implementation
                                        })
                
                # Check speech patterns if available
                if 'Speech' in char_profile:
                    speech_patterns = char_profile['Speech'].lower()
                    dialect_match = re.search(r'dialect[\s:]+(\w+)', speech_patterns)
                    
                    if dialect_match:
                        dialect = dialect_match.group(1)
                        # This would be expanded in a full implementation to check dialogue against dialect patterns
        
        return issues
    
    def _check_setting_consistency(self, content, file_path):
        """Check for setting consistency issues."""
        # Similar implementation to character consistency but for settings
        return []
    
    def _check_terminology_consistency(self, content, file_path):
        """Check for terminology consistency issues."""
        issues = []
        
        # Check for terms that are used in the content
        # Use our custom tokenizer instead of NLTK
        words = self._word_tokenize(content.lower())
        for term, definition in self.terminology.items():
            term_lower = term.lower()
            
            # Look for variations of the term
            term_variations = [term_lower, term_lower + 's', term_lower + 'es']
            
            for variation in term_variations:
                if variation in words:
                    # The term is used, now check if it's used consistently
                    # This is a simplified example - a real implementation would be more sophisticated
                    # Use our custom tokenizer instead of NLTK
                    sentences_with_term = [s for s in self._sent_tokenize(content) if variation in s.lower()]
                    
                    # Check for capitalization consistency for important terms
                    if term[0].isupper() and any(variation in s and not re.search(fr'\b{variation}\b', s.lower()) for s in sentences_with_term):
                        issues.append({
                            'type': 'consistency',
                            'severity': 'info',
                            'message': f"Terminology '{term}' should be capitalized consistently",
                            'file': file_path,
                            'line': None
                        })
        
        return issues 