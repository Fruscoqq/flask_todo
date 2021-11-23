#!/bin/bash

#activate virtual env
echo "Activating virtual enviroment"
source venv/bin/activate
echo

#Running pytest
echo "Running tests"
python3 -m pytest --cov=tests --cov-report term-missing
echo
