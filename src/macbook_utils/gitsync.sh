#!/usr/bin/env bash

REPO_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )/../.." &> /dev/null && pwd )
source $REPO_DIR/venv/bin/activate

export PYTHONPATH="$REPO_DIR/src/:$PYTHONPATH"

python $REPO_DIR/src/macbook_utils/gitsync.py $1
