SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_DIR/..
SRC_DIR=`pwd`
source $SCRIPT_DIR/../../venv/bin/activate

export PYTHONPATH="$SRC_DIR/:$PYTHONPATH"

python $SRC_DIR/macbook_utils/json_format.py "$1"
