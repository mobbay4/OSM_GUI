#!/bin/sh
#virtualenv --python=python3.7 venv
py -m pip install virtualenv
py -m virtualenv ./OSM_GUI_venv
py -m pip install -r requirements.txt