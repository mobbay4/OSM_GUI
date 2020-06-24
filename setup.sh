#!/bin/sh
#install virtual environment package -- just to be shure
py -m pip install virtualenv
#create a virtual environment in the application folder
py -m virtualenv ./OSM_GUI_venv
#install the required packages to the virtual environment
py -m pip install -r requirements.txt