#!/usr/bin/env bash

REPO_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )/../.." &> /dev/null && pwd )

if [ -d "$REPO_DIR/.venv" ]; then
    VENV_DIR="$REPO_DIR/.venv"
else
    VENV_DIR="$REPO_DIR/venv"
fi

source "$VENV_DIR"/bin/activate

export PYTHONPATH="$REPO_DIR/:$REPO_DIR/src/:$PYTHONPATH"

python $REPO_DIR/src/macbook_utils/$1.py $2
