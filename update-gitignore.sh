#!/bin/bash
# Script to handle gitignore configuration and remind about the interactive Multiverse structure setup process
#
# IMPORTANT:
# According to 00_setup_guide.md, the Multiverse directory structure should be:
# 1. Created through an interactive conversation with the AI assistant
# 2. Customized based on the user's project type, organization preference, and writing structure
# 3. NOT automatically generated with a predefined structure
#
# This script now focuses only on gitignore configuration and empty Multiverse directory

echo "Multiverse Directory Setup"
echo "==========================="
echo ""
echo "IMPORTANT: According to the setup rules, your Multiverse directory structure"
echo "should be created through an interactive conversation with the AI assistant."
echo ""
echo "The proper setup process includes:"
echo "1. Discussing your writing project type and purpose"
echo "2. Determining single vs. multi-project organization"
echo "3. Selecting appropriate writing structures/templates"
echo "4. Creating a CUSTOMIZED folder structure based on your specific needs"
echo ""
echo "This script will only create an empty Multiverse directory and configure gitignore settings."
echo "You should engage with the AI assistant for the interactive setup of your project structure."
echo ""

# Create empty Multiverse directory if it doesn't exist
if [ ! -d "Multiverse" ]; then
    echo "Creating empty Multiverse directory..."
    mkdir -p Multiverse
    echo "# Multiverse Directory - Structure to be created interactively" > Multiverse/.gitkeep
fi

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

echo ""
echo "Gitignore configuration complete!"
echo ""
echo "NEXT STEPS:"
echo "1. ENGAGE WITH THE AI ASSISTANT to create your custom Multiverse structure"
echo "   - Discuss your project type and goals"
echo "   - Select an appropriate writing structure"
echo "   - Design a folder organization that suits your specific needs"
echo ""
echo "2. BRANCH MANAGEMENT:"
echo "   - FOR WRITING: Use normal git commands to push content to GitHub"
echo "     'git push origin <branch-name>' to include ALL your writing content"
echo ""
echo "   - FOR TEMPLATE CHANGES: Use template mode to push to main"
echo "     './template-mode.sh on' before making template changes"
echo "     'git push origin HEAD:main' to push template changes"
echo "     './template-mode.sh off' to return to writing mode" 