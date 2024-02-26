SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_DIR/..
SRC_DIR=`pwd`
source $SCRIPT_DIR/../../venv/bin/activate

export PYTHONPATH="$SRC_DIR/:$PYTHONPATH"

if [ $# -eq 1 ]; then
    black "$1"
else
    python $SRC_DIR/macbook_utils/black_me.py
fi
