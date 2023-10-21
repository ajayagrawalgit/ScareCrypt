#!/bin/bash

# This script just triggers the python file.
# Made only to remove conflicts between pyton arguments if the user installs the tool locally on a Linux/MacOS Machine.

args=("$@")
python3 /usr/local/lib/ScareCrypt/scarecrypt.py $args