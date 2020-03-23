#!/bin/bash

echo making dev environment

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
cd $SCRIPTPATH
cd ..

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
