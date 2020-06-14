#
# AITPATH   version 1.0 / 14.6.20
#
# Copyright (c) 2019-2020, AI-Technologies - Rainer Wallwitz
# All rights reserved.
#
#
#
# This file is meant to be located inside the ipython extension folder, 
#
#     macos       : 'rainer/anaconda3/lib/python 3.7/site-packages/IPython/extensions'
#     win32       : C:\ProgramData\Anaconda3\lib\site-packages\IPython\extensions
#     win32 azure : \Users\DEBUDDSAOperator\Anaconda3\lib\site-packages\IPython\extensions
#
# and sets the path ensuring the application libs are found by ipython for execution.
#

import sys

def operatingSystem(): 
    azure = False
    # windows=win32  macos=darwin
    return 'darwin' if sys.platform=='darwin' else ('azure' if azure else 'windows' )

def sysUser():
    platform = operatingSystem()#sys.platform # windows=win32  macos=darwin
    if platform=='darwin':
        sys_user = 'rainer'
    else: # 'win32'
        sys_user = 'debuddsaoperator' if platform=='azure' else 'rwallwitz'
        sys_user += '/desktop/root'  
    return sys_user
sys_user = sysUser()

sys.path.append('/users/'+sys_user+'/Py/PyLibs/SpiritLibs')
sys.path.append('/users/'+sys_user+'/Py/PyLibs/SunFlowLibs')
sys.path.append('/users/'+sys_user+'/Py/PyLibs/TestLibs')

