# Author Workspace Server

A server component for the Author Workspace that monitors content changes, analyzes writing quality, and maintains consistency across writing projects.

## Features

- **Content Monitoring**: Watches for file changes in your writing workspace
- **Consistency Analysis**: Checks for character, setting, and terminology consistency
- **Style Analysis**: Evaluates writing style, readability, and voice consistency
- **Quality Assessment**: Identifies grammar, readability, and structural issues
- **Plagiarism Detection**: Checks for self-plagiarism and potential AI-generated content
- **Web Interface**: Provides a browser-based dashboard for viewing analysis results

## Installation

1. Make sure you have Python 3.9 or higher installed.

2. Install the required dependencies:

```bash
cd .cursor/Server
pip install -r requirements.txt
```

3. Download NLTK data (required for text analysis):

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('averaged_perceptron_tagger')"
```

4. Download spaCy model (for more advanced NLP tasks):

```bash
python -m spacy download en_core_web_sm
```

## Usage

### Continuous Monitoring

To start the server in continuous monitoring mode (watches for file changes):

```bash
cd .cursor/Server
python app.py --mode continuous
```

Then open your web browser and navigate to `http://localhost:5000` to view the web interface.

### Batch Analysis

To run a one-time analysis on a specific file or directory:

```bash
cd .cursor/Server
python app.py --mode batch --target "Projects/MyNovel"
```

### Pre-Submission Check

To validate a specific file before finalizing:

```bash
cd .cursor/Server
python app.py --mode validate --target "Projects/MyNovel/Manuscript/Chapter03.md"
```

## Server Configuration

The server can be configured by editing the `config.yml` file. Key settings include:

- `workspace_root`: Path to the author workspace root
- `monitoring.enabled`: Whether to enable file system monitoring
- `monitoring.ignore_patterns`: File patterns to ignore
- `analysis.consistency_check`: Whether to check narrative consistency
- `analysis.style_check`: Whether to check writing style
- `analysis.quality_check`: Whether to check writing quality
- `analysis.originality_check`: Whether to check for plagiarism

## Integration with Author Workspace

The server is designed to work seamlessly with the Author Workspace structure:

- It recognizes both single-project and multi-project workspace structures
- It reads character profiles, setting descriptions, and terminology definitions from the appropriate directories
- It understands the writing templates and narrative structures defined in the workspace

## Extending the Server

The server is designed to be extensible:

1. Add new analyzers in the `analyzers/` directory
2. Customize analysis rules in the configuration file
3. Extend the web interface in the `web/` directory

## Troubleshooting

If you encounter issues:

1. Check the server console output for error messages
2. Verify the workspace directory structure matches what the server expects
3. Ensure all dependencies are properly installed
4. Check if there are any file permission issues

## Contributing

This server is part of the Author Workspace template. Contributions are welcome! 

## License

This project is licensed under the MIT License. 