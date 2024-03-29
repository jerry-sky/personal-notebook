import getpass
import os
import pathlib

# home directory
HD = os.path.expanduser('~')
# user’s config directory
HDC = HD + '/.config'
RHD = '/root'
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
# Ubuntu
UBU = CD + '/ubuntu'
# fixes for external programs and such
FXD = CD + '/fixes'

# username
USER = getpass.getuser()
