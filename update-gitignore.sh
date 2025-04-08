#!/bin/bash
# Script to update gitignore files with content directories

# Ensure the Author directory exists
if [ ! -d "./Author" ]; then
    echo "Creating Author directory..."
    mkdir -p ./Author
fi

# Update .gitignore
if [ -f .gitignore ]; then
    echo "Checking .gitignore file..."
    
    # Check if the Author directory is already in .gitignore
    if ! grep -q "/Author/" .gitignore; then
        echo -e "\n# Author content directory - contains all writing content" >> .gitignore
        echo "/Author/" >> .gitignore
        echo "Added Author/ to .gitignore"
    else
        echo "Author/ already in .gitignore"
    fi
else
    # Create .gitignore if it doesn't exist
    echo "Creating .gitignore file..."
    cat > .gitignore << EOL
# macOS system files
.DS_Store
.AppleDouble
.LSOverride
Icon
._*

# Python virtual environment
venv/
__pycache__/
*.py[cod]
*$py.class
*.so

# Editor files
.vscode/
.idea/
*.swp
*.swo

# Logs and databases
*.log
*.sqlite
*.sqlite3
*.db

# User-specific workspace configurations
*.code-workspace.user

# Author content directory - contains all writing content
/Author/

# Add a gitignore-template file to selectively ignore content
.gitignore-template
EOL
    echo "Created .gitignore with Author/ directory ignored"
fi

# Update .gitignore-template
if [ -f .gitignore-template ]; then
    echo "Checking .gitignore-template file..."
    
    # Check if the Author directory is already in .gitignore-template
    if ! grep -q "/Author/" .gitignore-template; then
        echo -e "\n# Author content directory - contains all writing content" >> .gitignore-template
        echo "/Author/" >> .gitignore-template
        echo "Added Author/ to .gitignore-template"
    else
        echo "Author/ already in .gitignore-template"
    fi
else
    # Create .gitignore-template if it doesn't exist
    echo "Creating .gitignore-template file..."
    cat > .gitignore-template << EOL
# This file is used when you want to push template improvements
# It excludes all writing content but includes template and server files

# Author content directory - contains all writing content
/Author/

# Keep system files excluded
.DS_Store
.AppleDouble
.LSOverride
Icon
._*
__pycache__/
*.py[cod]
*$py.class
.vscode/
.idea/
EOL
    echo "Created .gitignore-template with Author/ directory ignored"
fi

echo "GitIgnore files updated successfully." 