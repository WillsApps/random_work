/Users/wburdett/.PyCharm/scratches/extensions/mine/_aliases/black_me.sh

args_concatenate=""
for arg in "$@"; do
    # Remove double quotes and replace with single quotes
    arg="${arg//\"/\'\'}"

    # Concatenate the arguments with a space separator
    args_concatenated="${args_concatenated} ${arg}"
done
git add .
git commit -m "${args_concatenated}"
git push
