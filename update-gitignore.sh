#!/bin/bash
# Script to create and maintain the Multiverse directory structure

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