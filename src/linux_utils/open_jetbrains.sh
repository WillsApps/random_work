#!/usr/bin/env bash

PROGRAM=$1
VERSION=$(ls -l ~/Programs/ | grep $PROGRAM | rev | cut -d' ' -f 1 | rev)
echo $VERSION
DIR=$(basename "$(pwd)")
cd ..
PARENT_DIR=$(basename "$(pwd)")

if [ "$PARENT_DIR" = "Code" ]; then
  NAME="$PROGRAM-$DIR"
  TARGET="$(pwd)"
fi

cd "$DIR" || exit
PROGRAM_PATH="$HOME/Programs/$VERSION/bin/$PROGRAM"
if [ ! -f $PROGRAM_PATH ]; then
  PROGRAM_PATH="$PROGRAM_PATH.sh"
fi
screen -S "$PROGRAM" -d -m $PROGRAM_PATH $TARGET
