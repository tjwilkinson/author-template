#!/bin/bash
# Script to update gitignore files with content directories

# Get a list of top-level directories that are likely content folders
# Excludes .git, .cursor, docs which are template/system directories
CONTENT_DIRS=$(find . -maxdepth 1 -type d -not -path "./.*" -not -path "./docs" -not -path "." | sort)

# Update .gitignore
if [ -f .gitignore ]; then
    echo "Updating .gitignore with content directories..."
    
    # Check if the writing content section exists
    if ! grep -q "# Writing content directories" .gitignore; then
        # Add the section if it doesn't exist
        echo -e "\n# Writing content directories (excluded from template updates)" >> .gitignore
    fi
    
    # Add each content directory if not already present
    for DIR in $CONTENT_DIRS; do
        DIR_NAME=$(basename "$DIR")
        if ! grep -q "/$DIR_NAME/" .gitignore; then
            echo "/$DIR_NAME/" >> .gitignore
            echo "Added $DIR_NAME to .gitignore"
        fi
    done
fi

# Update .gitignore-template
if [ -f .gitignore-template ]; then
    echo "Updating .gitignore-template with content directories..."
    
    # Check if the writing content section exists
    if ! grep -q "# Writing content directories" .gitignore-template; then
        # Add the section if it doesn't exist
        echo -e "\n# Writing content directories" >> .gitignore-template
    fi
    
    # Add each content directory if not already present
    for DIR in $CONTENT_DIRS; do
        DIR_NAME=$(basename "$DIR")
        if ! grep -q "/$DIR_NAME/" .gitignore-template; then
            echo "/$DIR_NAME/" >> .gitignore-template
            echo "Added $DIR_NAME to .gitignore-template"
        fi
    done
fi

echo "GitIgnore files updated successfully." 