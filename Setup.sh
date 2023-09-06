#!/bin/bash

# figure out user's bash type
# Get the system name using uname
sysname="$(uname -s)"

# Check if the system is Ubuntu
if [ "$sysname" == "Linux" ] && [ -f /etc/lsb-release ]; then
    # Check for the presence of the lsb-release file, which is common in Ubuntu.
    echo "You are on Ubuntu."
    source src/Ubuntu.sh
elif [ "$sysname" == "Darwin" ]; then
    echo "You are on macOS."
    source src/Macos.sh
else
    echo "Unsupported system: $sysname"
fi

