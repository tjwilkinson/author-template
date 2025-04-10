#!/bin/bash

# Script to convert all PDFs in References directory that don't have corresponding MD files
# Uses the PDF-to-markdown conversion API endpoint we set up

# Check if the server is running
if ! curl -s http://localhost:5555 > /dev/null; then
  echo "Error: Server is not running on port 5555. Please start the server first."
  echo "cd .cursor/Server && source fresh_venv/bin/activate && python3 app.py --port 5555"
  exit 1
fi

# Directory to search for PDFs
SEARCH_DIR="Multiverse/AuthorResources/References"

# Find all PDFs and check if they have corresponding MD files
echo "Finding PDFs without corresponding markdown files..."
COUNTER=0
CONVERTED=0

# Save the current IFS
OLDIFS="$IFS"

# Set IFS to newline only
IFS=$'\n'

# Find all PDFs and process each one
for PDF_PATH in $(find "$SEARCH_DIR" -name "*.pdf"); do
  COUNTER=$((COUNTER + 1))
  
  # Determine if a corresponding MD file exists
  MD_PATH="${PDF_PATH%.pdf}.md"
  
  if [ ! -f "$MD_PATH" ]; then
    echo "Converting: $PDF_PATH"
    
    # Create JSON with escaped path
    JSON="{\"pdf_path\": \"$PDF_PATH\"}"
    
    # Call the API to convert the PDF
    RESPONSE=$(curl -s -X POST -H "Content-Type: application/json" -d "$JSON" http://localhost:5555/api/convert_pdf)
    
    # Check if the markdown file was created
    if [ -f "$MD_PATH" ]; then
      echo "✅ Conversion successful: $MD_PATH"
      CONVERTED=$((CONVERTED + 1))
    else
      echo "❌ Conversion failed: $RESPONSE"
    fi
    
    # Slight delay to not overwhelm the server
    sleep 1
  else
    echo "Skipping (already exists): $PDF_PATH"
  fi
done

# Restore the original IFS
IFS="$OLDIFS"

echo ""
echo "Summary:"
echo "- PDFs found: $COUNTER"
echo "- PDFs converted: $CONVERTED"
echo "- PDFs skipped (already had MD): $((COUNTER - CONVERTED))"
echo ""
echo "Conversion complete!" 