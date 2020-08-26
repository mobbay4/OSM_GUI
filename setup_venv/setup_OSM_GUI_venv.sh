# ###############################################################################################
#
#  This Script is to set up the environment "OSM_GUI_venv" and the packages deeded in it 
#
#    Location: Anaconda3\envs\OSM_GUI_venv
#    
#  NOTE: - for adding new packages to the environment add them to the requierements
#             --> (if there is a conda version --> requierements_conda.txt // otherwise requirements_pip.txt)
#        - anaconda recoments to generate the environment new, if a conda package has to be added after a pip package
#           https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#using-pip-in-an-environment
#         
# ###############################################################################################
#
# ###############################################################################################
# handle virtual environment
# ###############################################################################################
#
# - To create the environment use:
#conda create --name "OSM_GUI_venv"   
#
# - To activate this environment, use
#conda activate OSM_GUI_venv
#
# - To deactivate an active environment, use
#conda deactivate
#
# - To delete the environment
#conda remove --name OSM_GUI_venv --all 
# - To verify that the environment was removed, in your terminal window or an Anaconda Prompt, run:
#conda info --envs
#
#
# ###############################################################################################
# package section --> run requirements
# ###############################################################################################
#conda install --file requirements_conda.txt
#pip install -r requirements_pip.txt
#
# ###############################################################################################
# distribute environment with yml-file (for Anaconda only)
# ###############################################################################################
#
## - To export the environment run following line Anaconda-Prompt with activated environment:
#conda env export > environment.yml
#
## - create enviroment from yml-file
#conda env create -f environment.yml
#
# ###############################################################################################
# create jupyter notebook kernel in this virtual environment 
# ###############################################################################################
#   manual: https://anbasile.github.io/programming/2017/06/25/jupyter-venv/
# Note: --> ipython package must be installed with requirements_cond.txt
#
## check this line next time (with activated enviroment):
#python -m ipykernel install
## the old one has a problem with the "--user" parameter:
## jupyter notebook cernel can not be started from VScode then
# ipython kernel install --user --name=OSM_GUI_venv