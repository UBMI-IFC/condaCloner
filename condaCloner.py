#!/usr/bin/python3
# -*- coding: us-ascii -*-
#
# ------------------------------
# Name:        condaCloner.py
# Purpose:     Backup all conda environments of a computer as a series of yml files
#
# @uthor:      Carlos Alberto Peralta Alvarez cperalta@ifc.unam.mx
#
# Created:     Fri 10 Dec 2021
# Copyright:   (c) Carlos Alberto Peralta Alvarez 2021
# Licence:     GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007
# ------------------------------
""" Tool to create a folder of yml files to create an snapshot of a Conda environments on a computer"""

from subprocess import check_output
from socket import gethostname
from datetime import date
from pathlib import Path
 
OUTPUT_DIR = Path("/home/cperalta/Documents/testConda/py_conda_tests") # directory for tests
#OUTPUT_DIR = Path("/UBMInas/SEISbio_conda_env_backups/tmp")

# Get date and host info for definitive output dir
host_id = gethostname()
backup_date = str(date.today()).replace("-","")

# Create output directory
out_dir = OUTPUT_DIR / ('conda_backup_' + backup_date)  / (host_id + "_" + backup_date)
out_dir.mkdir(parents = True, exist_ok = True)

# Get environments paths and names for yml creation
env = check_output(['conda','info','-e']).decode()
env = env.replace('*','')

#env = env[env.rfind('#')+1:].split() # to backup all env
env = env[env.find('base'):].split() # to backup main conda installation environments only
#env = env[env.rfind('#')+1:env.find('base')-1].split() # to backup user env only

env_path= env[1:len(env):2]
env_name= env[0:len(env):2]
env_yml= [str(out_dir) + "/" + s + ".yml" for s in env_name]

for i in range(len(env_yml)):
    yml = check_output(['conda', 'env', 'export','-p',env_path[i]]).decode()
    yml = yml.partition('prefix:')[0]
    yml = yml.replace('null', env_name[i])
    with open (env_yml[i], 'w') as f :
        f.write(yml)

#if __name__ == '__main__':
#    main()
