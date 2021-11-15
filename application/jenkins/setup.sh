#!/bin/bash

#install apt dependencies
echo "Installing apt dependencies"
sudo apt update
sudo apt install python3-venv python3-pip python3 -y
echo

#activate virtual env
echo "Activating virtual enviroment"
source venv/bin/activate
echo

#install requirements
echo "Installing reqiurements.txt"
pip3 install -r requirements.txt
echo
