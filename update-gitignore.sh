#!/bin/bash
# Script to create and maintain the Multiverse directory structure
#
# IMPORTANT:
# This script creates the Multiverse directory structure and ensures that:
# 1. In writing/universe branches: Content files (.md, .txt, .docx) are properly tracked
#    - When in writing mode (.gitignore is normal), your content will be pushed with 'git push'
# 2. In template mode: Content files are ignored when pushing to main
#    - When in template mode (after ./template-mode.sh on), content changes are ignored 
#      when pushing to main using 'git push origin HEAD:main'
#
# Run this script in a new branch to set up the directory structure

# Create the Multiverse directory structure
echo "Creating Multiverse directory structure..."

# Create main directories
mkdir -p Multiverse/Series
mkdir -p Multiverse/Education
mkdir -p Multiverse/Shared/Characters
mkdir -p Multiverse/Shared/Settings
mkdir -p Multiverse/Shared/Timeline
mkdir -p Multiverse/Meta

# Add placeholder files to track the directories in git
echo "# Series Directory" > Multiverse/Series/.gitkeep
echo "# Education Directory" > Multiverse/Education/.gitkeep
echo "# Shared Characters Directory" > Multiverse/Shared/Characters/.gitkeep
echo "# Shared Settings Directory" > Multiverse/Shared/Settings/.gitkeep
echo "# Shared Timeline Directory" > Multiverse/Shared/Timeline/.gitkeep
echo "# Meta Directory" > Multiverse/Meta/.gitkeep

# Update .gitignore if needed
if [ -f .gitignore ]; then
    echo "Checking .gitignore file..."
    
    # Make sure the Multiverse structure patterns exist
    if ! grep -q "/Multiverse/\*\*/\*\.md" .gitignore; then
        cat >> .gitignore << EOL

# Ignore writing content files within Multiverse, but keep the structure
/Multiverse/**/*.md
/Multiverse/**/*.txt
/Multiverse/**/*.docx

# Preserve the Multiverse directory structure
!/Multiverse/
!/Multiverse/*/
!/Multiverse/*/*/
EOL
        echo "Updated .gitignore with Multiverse patterns"
    else
        echo "Multiverse patterns already in .gitignore"
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

# Python
__pycache__/
*.py[cod]
*$py.class

# Editor files
.vscode/
.idea/
*.swp
*.swo

# Logs and databases
*.log
*.sqlite
*.db

# Ignore writing content files within Multiverse, but keep the structure
/Multiverse/**/*.md
/Multiverse/**/*.txt
/Multiverse/**/*.docx

# Preserve the Multiverse directory structure
!/Multiverse/
!/Multiverse/*/
!/Multiverse/*/*/

# Add a gitignore-template file to selectively ignore content
.gitignore-template
EOL
    echo "Created .gitignore with Multiverse patterns"
fi

# Update .gitignore-template the same way
if [ -f .gitignore-template ]; then
    echo "Checking .gitignore-template file..."
    
    # Make sure the Multiverse structure patterns exist
    if ! grep -q "/Multiverse/\*\*/\*\.md" .gitignore-template; then
        cat >> .gitignore-template << EOL

# Ignore writing content files within Multiverse, but keep the structure
/Multiverse/**/*.md
/Multiverse/**/*.txt
/Multiverse/**/*.docx

# Preserve the Multiverse directory structure
!/Multiverse/
!/Multiverse/*/
!/Multiverse/*/*/
EOL
        echo "Updated .gitignore-template with Multiverse patterns"
    else
        echo "Multiverse patterns already in .gitignore-template"
    fi
else
    # Create .gitignore-template if it doesn't exist
    echo "Creating .gitignore-template file..."
    cp .gitignore .gitignore-template
    sed -i.bak '1s/^/# This file is used when you want to push template improvements\n# It contains the same rules as the regular gitignore\n\n/' .gitignore-template
    rm -f .gitignore-template.bak
    echo "Created .gitignore-template with Multiverse patterns"
fi

echo "Multiverse directory structure setup complete!"
echo ""
echo "IMPORTANT WORKFLOW NOTES:"
echo "1. FOR WRITING BRANCHES: Use normal git commands to push content to GitHub"
echo "   - Use 'git push origin <branch-name>' to include ALL your writing content"
echo ""
echo "2. FOR TEMPLATE CHANGES: Use template mode to push to main"
echo "   - Run './template-mode.sh on' before making template changes"
echo "   - Push template changes with 'git push origin HEAD:main'"
echo "   - Run './template-mode.sh off' to return to writing mode" 