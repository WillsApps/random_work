#!/usr/bin/env bash

TARGET="$HOME/.bashrc"

LINE_TO_FIND="\$HOME/Code/random_work/src/linux_utils/.bash_aliases"

INSTALL="
if [ -f \$HOME/Code/random_work/src/linux_utils/.bash_aliases ]; then
    . \$HOME/Code/random_work/src/linux_utils/.bash_aliases
    . \$HOME/Code/random_work/src/linux_utils/.bash_exports
fi
"

if [[ -z $(grep "$LINE_TO_FIND" "$TARGET") ]]
then
  echo "$INSTALL" >> "$TARGET"
  echo "Installed!"
else
  echo "Already installed!"
fi
