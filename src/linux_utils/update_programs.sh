#!/usr/bin/env bash

REPO_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )/../.." &> /dev/null && pwd )
echo $REPO_DIR
if [ -d "$REPO_DIR/.venv" ]; then
    VENV_DIR="$REPO_DIR/.venv"
else
    VENV_DIR="$REPO_DIR/venv"
fi

source "$VENV_DIR"/bin/activate

export PYTHONPATH="$REPO_DIR/:$PYTHONPATH"
export PYTHONPATH="$REPO_DIR/src/:$PYTHONPATH"
python "$REPO_DIR"/src/linux_utils/update_programs.py