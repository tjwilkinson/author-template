#!/bin/bash

# Start the Author Workspace Server
# This script activates the virtual environment and starts the server

# Directory of this script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Activate the virtual environment
source "$SCRIPT_DIR/venv/bin/activate"

# Default port
PORT=5000

# Parse command line arguments
MODE="continuous"
TARGET=""

# Process arguments
while [[ $# -gt 0 ]]; do
  key="$1"
  case $key in
    --mode)
      MODE="$2"
      shift
      shift
      ;;
    --target)
      TARGET="$2"
      shift
      shift
      ;;
    --port)
      PORT="$2"
      shift
      shift
      ;;
    *)
      echo "Unknown option: $1"
      exit 1
      ;;
  esac
done

# Start the server
if [ -z "$TARGET" ]; then
  echo "Starting server in $MODE mode on port $PORT..."
  python3 "$SCRIPT_DIR/app.py" --mode "$MODE" --port "$PORT"
else
  echo "Starting server in $MODE mode for target '$TARGET' on port $PORT..."
  python3 "$SCRIPT_DIR/app.py" --mode "$MODE" --target "$TARGET" --port "$PORT"
fi 