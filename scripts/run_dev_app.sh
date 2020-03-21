#!/usr/bin/env bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
cd $SCRIPTPATH
cd ..

source venv/bin/activate
cd src
export PYTHONPATH="$PWD"
cd ..
python run.py dev_tools/config.yml
