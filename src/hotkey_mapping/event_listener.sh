#!/usr/bin/env bash
MODULE_DIR=$(dirname  "${BASH_SOURCE[0]}")
REPO_DIR=$( cd -- "$MODULE_DIR/../.." &> /dev/null && pwd )
BASH_NAME=$(basename "$0")
PYTHON_NAME=$(echo $BASH_NAME | sed -En "s/.sh/.py/p")
$MODULE_DIR/helper.sh $PYTHON_NAME