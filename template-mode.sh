#!/bin/bash
# Script to switch between writing mode and template mode

MODE=$1

if [ "$MODE" == "on" ]; then
    echo "Switching to TEMPLATE MODE"
    echo "In this mode, writing content changes will be ignored, only template/server changes will be tracked"
    cp .gitignore-template .gitignore
    git add .gitignore
    git commit -m "Switch to template mode"
    echo "Template mode activated. Make your template/server changes now."
    echo "When ready to push template changes, use:"
    echo "git push origin HEAD:main"
elif [ "$MODE" == "off" ]; then
    echo "Switching back to WRITING MODE"
    git checkout -- .gitignore
    git commit -m "Switch back to writing mode"
    echo "Writing mode activated. All your content changes will be tracked again."
else
    echo "Usage: ./template-mode.sh [on|off]"
    echo "  on  - Switch to template mode (ignores writing content)"
    echo "  off - Switch back to writing mode (tracks all content)"
fi 