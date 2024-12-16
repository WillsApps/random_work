#/usr/bin/sh

PROGRAM=$1
VERSION=$2
DIR=$(basename "$(pwd)")
cd ..
PARENT_DIR=$(basename "$(pwd)")
cd "$DIR" || exit

if [ "$PARENT_DIR" != "Code" ]
then
  screen -S pycharm -d -m "/home/aggy/Programs/$PROGRAM-$VERSION/bin/$PROGRAM"
  echo "Generically opening $PROGRAM"
  exit 0
fi


sc
cd "$DIR" || exitreen -S "$PROGRAM-$DIR" -d -m "/home/aggy/Programs/$PROGRAM-$VERSION/bin/$PROGRAM" "$(pwd)"