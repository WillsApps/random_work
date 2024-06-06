#!/bin/bash

ARGS_CONCATENATE=""
for arg in "$@"; do
    # Remove double quotes and replace with single quotes
    arg="${arg//\"/\'\'}"

    # Concatenate the arguments with a space separator
    ARGS_CONCATENATE="${ARGS_CONCATENATE} ${arg}"
done


function addFolders()
{
  FOLDERS=("dags" "tests" "src")
  for folder in "${FOLDERS[@]}"
  do
    if [ -d "$folder" ]; then
      git add "$folder"
    fi
  done
}


addFolders
git commit -m "${ARGS_CONCATENATE}"
addFolders
git commit -m "${ARGS_CONCATENATE}"
git push

date "+%Y-%m-%d %H:%M:%S"