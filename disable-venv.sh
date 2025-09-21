# Guard statement to exit early if not in venv
# ONLY WORKS ON LINUX
if [ -z "$VIRTUAL_ENV" ]; then
    return
fi

# Deactivate venv
echo "Deactivating venv..."
deactivate \
    || { echo "venv deactivation failed"; return 1; }
