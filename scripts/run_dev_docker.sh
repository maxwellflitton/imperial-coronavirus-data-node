#!/usr/bin/env bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
cd $SCRIPTPATH
cd ..

cd dev_tools
docker stop $(docker ps -a -q)
docker-compose up