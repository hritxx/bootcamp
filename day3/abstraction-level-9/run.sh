#!/bin/bash

if [ "$1" == "--watch" ]; then
  python3 main.py --watch
elif [ "$1" == "--input" ]; then
  python3 main.py --input "$2"
else
  echo "Usage: ./run.sh --watch OR ./run.sh --input filename.txt"
fi
