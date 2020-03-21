#!/usr/bin/env bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
cd $SCRIPTPATH
cd ..
python3 -m venv venv
source venv/bin/activate

cd src
export PYTHONPATH=$PYTHONPATH:$(pwd)
cd ..

cd tests
python -m unittest discover tests