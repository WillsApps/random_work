#!/usr/bin/bash
list=$(ps -ef | grep PathOfExileSteam.exe | grep steam | cut -d' ' -f7)
while IFS= read -r line; do
    mullvad split-tunnel add $line
    echo "mullvad split-tunnel add $line"
done <<< "$list"
