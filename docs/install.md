# install environment for OSM_GUI
- [1. install Anaconda](#1-install-anaconda)
- [2. create virtual environment](#2-create-virtual-environment)
- [3. install python without Anaconda](#3-install-python-without-anaconda)

you need:

- a python installation (prefered 3.8.0 -- at least a windows launcher must be included)
- a virtual environment with all packages of [requirements](../requirements.txt)

To get both, simply follow the next chapters.

## 1. install Anaconda

The most easy way to get a stable python environment is to use Anaconda.

So Install Anaconda on your PC.

## 2. create virtual environment

Manually run steps from [setup_OSM_GUI_venv.sh](../setup_OSM_GUI_venv.sh)

Manually meas to copy the lines to the `Anaconda Prompt` and execute them.

## 3. install python without Anaconda

If you do not have a python version now:

- got to  [download python](https://www.python.org/downloads/windows/), and download `Windows x86-64 executable installer` or [directly download it](https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe)
- run the installer.exe as-*Administrator**
- toggle on-**Install launcher for all users*** and choose-**Install Now*** ![installation settings](./pictures/python_win_installer.png)
- open cmd prompt or PowerShell and type py --> if no error occurs, python is installed correctly
