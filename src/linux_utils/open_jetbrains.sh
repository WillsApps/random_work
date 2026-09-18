#!/usr/bin/env bash

PROGRAM=$1
VERSION=$(ls -ltr ~/Programs/ | grep $PROGRAM | tail -1 | rev | cut -d' ' -f 1 | rev)
ORIGINAL_DIR="$(pwd)"
DIR=$(basename "$(pwd)")
cd ..
PARENT_DIR=$(basename "$(pwd)")
TARGET=""
if [ "$PARENT_DIR" = "Code" ]; then
  NAME="$PROGRAM-$DIR"
  TARGET=$ORIGINAL_DIR
fi

cd "$DIR" || exit
PROGRAM_PATH="$HOME/Programs/$VERSION/bin/$PROGRAM"
if [ ! -f $PROGRAM_PATH ]; then
  PROGRAM_PATH="$PROGRAM_PATH.sh"
fi
screen -S "$PROGRAM" -d -m $PROGRAM_PATH $TARGET
