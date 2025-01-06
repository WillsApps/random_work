#!/usr/bin/env bash

REPO_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )/../.." &> /dev/null && pwd )

python $REPO_DIR/src/macbook_utils/run_local.py json_format "$*"
