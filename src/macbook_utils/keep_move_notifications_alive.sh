#!/usr/bin/env bash

REPO_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )/../.." &> /dev/null && pwd )

"$REPO_DIR"/src/macbook_utils/run_local.sh keep_move_notifications_alive
