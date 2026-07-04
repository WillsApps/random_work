#!/bin/bash

STR="$(pwd)"
SUB='/Code/'

if [[ "$STR" != *"$SUB"* ]]; then
  cd $HOME/Code/random_work/
fi

COMMAND="rm -rf $(pwd)/.idea"
echo $COMMAND
$COMMAND
$HOME/Programs/pycharm-2025.3.1.1/bin/pycharm $(pwd)
