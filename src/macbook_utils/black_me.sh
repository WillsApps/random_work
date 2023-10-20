source /Users/Shared/web/random_work/venv/bin/activate

if [ $# -eq 1 ]; then
    black "$1"
else
    python /Users/wburdett/.PyCharm/scratches/extensions/mine/_aliases/black_me.py
fi
