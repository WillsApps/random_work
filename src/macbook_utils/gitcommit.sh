#!/usr/bin/env bash

CURRENT_BRANCH=git branch | grep "*" | cut -d ' ' -f 2

if [ "$(git branch --list main)" ]
then
  MAIN="main"
else
  MAIN="develop"
fi

if [ "$CURRENT_BRANCH" == $MAIN ]
then
  git pull
  exit 0
fi

git checkout $MAIN
git pull
git checkout "$CURRENT_BRANCH"

ARGS_CONCATENATE=""
for arg in "$@"; do
    # Remove double quotes and replace with single quotes
    arg="${arg//\"/\'\'}"

    # Concatenate the arguments with a space separator
    ARGS_CONCATENATE="${ARGS_CONCATENATE} ${arg}"
done
if [ "$ARGS_CONCATENATE" == "" ]
then
  exit 0
fi
git add .
git commit -m "${ARGS_CONCATENATE}"
git push
