#!/usr/bin/env bash

REPO_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )/../.." &> /dev/null && pwd )

if [ -d "$REPO_DIR/.venv" ]; then
    VENV_DIR="$REPO_DIR/.venv"
else
    VENV_DIR="$REPO_DIR/venv"
fi
source "$VENV_DIR"/bin/activate

sqlfluff format --dialect databricks $1