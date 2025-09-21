#!/usr/bin/env bash
# NOTE: use with source or .

VENV_DIR=".venv"

# Guard statement to exit early if already in venv
if [ -n "$VIRTUAL_ENV" ]; then
    return
fi

# Create venv if directory doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating venv at '$VENV_DIR'..."
    python -m venv "$VENV_DIR" \
    || { echo "venv creation failed"; return 1; }
fi

# Activate venv
echo "Activating venv..."
source "$VENV_DIR/bin/activate" \
|| { echo "venv activation failed"; return 1; }

# Upgrade dependencies
echo "Installing and upgrading dependencies..."
(pip install --upgrade pip && pip install --upgrade -r requirements.txt) \
    || { echo "pip install failed"; return 1; }
