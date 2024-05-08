#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
"$SCRIPT_DIR"/gitdev.sh

TICKET=$1

ARGS_CONCATENATE=""
for arg in "$@"; do
    if [ "$arg" != "$TICKET" ]
    then
      # Remove double quotes and replace with single quotes
      arg=$(echo "$arg" | tr -cd '[:alnum:]_')

      if [ "$arg" != "" ]
      then

        # Concatenate the arguments with a space separator
        if [ "$ARGS_CONCATENATE" == "" ]
        then
          ARGS_CONCATENATE=$arg
        else
          ARGS_CONCATENATE="${ARGS_CONCATENATE}_${arg}"
        fi
      fi
    fi
done
if [ "$ARGS_CONCATENATE" == "" ]
then
  exit 0
fi
echo "DATAI-$TICKET/$ARGS_CONCATENATE"
#git add .
#git commit -m "${ARGS_CONCATENATE}"
#git push
