# Data Processing Node
This is a repo for managing the build and serving of a server that processes data. 

## Structure 
- The server uses ```travis``` for running the unit tests on pull requests. 
- The database is MySQL which is ran in docker-compose.
- The cache uses Redis for task queuing which is ran in docker-compose. 
- Gunicorn is used to queue requests for the Flask app and convert the requests to python objects. 
- NGINX is used to queue requests to the system.

## Setup
- setup the python virtual environment: bash script => ```scripts/create_venv.sh```

## Running 

- Run all unit tests: bash script => ```scripts/run_unit_tests.sh```
- Run dev environment: bash script => ```scripts/run_dev_docker.sh```
- Run dev server: bash script => ```scripts/run_dev_app.sh```
