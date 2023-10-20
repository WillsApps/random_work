source /Users/Shared/web/random_work/venv/bin/activate

if [ $# -eq 1 ]; then
    python /Users/wburdett/.PyCharm/scratches/extensions/mine/_aliases/sql_me.py "$1"
else
    python /Users/wburdett/.PyCharm/scratches/extensions/mine/_aliases/sql_me.py
fi
