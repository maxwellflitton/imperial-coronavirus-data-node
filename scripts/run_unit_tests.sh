#!/usr/bin/env bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
cd $SCRIPTPATH
cd ..
source venv/bin/activate
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
#cd tests

python -m unittest discover tests
