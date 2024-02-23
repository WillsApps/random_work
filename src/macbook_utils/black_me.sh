source /Users/will.burdett/projects/random_work/venv/bin/activate

export PYTHONPATH="/Users/will.burdett/projects/random_work/src/:$PYTHONPATH"

if [ $# -eq 1 ]; then
    black "$1"
else
    python /Users/will.burdett/projects/random_work/src/macbook_utils/black_me.py
fi
