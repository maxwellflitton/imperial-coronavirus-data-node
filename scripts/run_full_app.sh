#!/usr/bin/env bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
cd $SCRIPTPATH
cd ..

docker stop $(docker ps -a -q)
docker-compose build flask
docker-compose up