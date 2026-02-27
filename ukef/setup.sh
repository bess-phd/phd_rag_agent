#!/bin/bash
# helper script to prepare the Python environment for the UKEF agent

set -e

# create virtual environment if it doesn't already exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
else
    echo "Using existing virtual environment (skipping creation)"
fi

# shellcheck disable=SC1091
. .venv/bin/activate

echo "Upgrading pip, setuptools, and wheel..."
pip install --upgrade pip setuptools wheel

echo "Installing required packages from requirements.txt..."
pip install -r requirements.txt

# Azure CLI is useful for `az login` but its dependencies conflict
# with our pinned azure-ai-projects version.  It's better to install
# the CLI globally or with --no-deps rather than in this venv.
# If you must install it here, uncomment the next line:
# pip install azure-cli --no-deps || true

echo ""
echo "========================================"
echo "Environment is ready!"
echo "========================================"
echo "Activate using:  source .venv/bin/activate"
echo "Run the agent:   python run_agent.py"
echo ""