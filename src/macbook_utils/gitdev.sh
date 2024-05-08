#!/usr/bin/env bash

if [ "$(git branch --list main)" ]
then
  MAIN="main"
else
  MAIN="develop"
fi

git checkout $MAIN
git pull
