#!/usr/bin/env bash

MODULE_DIR=$(dirname  "${BASH_SOURCE[0]}")
REPO_DIR=$( cd -- "$MODULE_DIR/../.." &> /dev/null && pwd )

if [[ $(/usr/bin/id -u) -ne 0 ]]; then
    echo "Not running as root"
    exit
fi

if [ -d "$REPO_DIR/.venv" ]; then
    VENV_DIR="$REPO_DIR/.venv"
else
    VENV_DIR="$REPO_DIR/venv"
fi

source "$VENV_DIR"/bin/activate

export PYTHONPATH="src/:$PYTHONPATH"
python "$MODULE_DIR/$1"