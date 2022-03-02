import getpass
import os
import pathlib

# home directory
HD = os.path.expanduser('~')
# root config directory
CD = str(pathlib.Path().absolute())
# installation script directory
ISD = CD + '/install-scripts'
# config files directory
CFD = CD + '/config-files'
# utility scripts directory
USD = CD + '/utility-scripts'
# second-keyboard directory
SKD = CD + '/second-keyboard'
# audio directory
AUD = CD + '/audio'
# Xinput configs
XIN = CD + '/xinput'

# username
USER = getpass.getuser()
