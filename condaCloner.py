# Conda environment cloner (python version)

import os
import subprocess
import socket
from datetime import date

OUTPUT_DIR = "/home/cpa/Documentos/testConda/py_conda_tests" # directory for tests
#OUTPUT_DIR = "/UBMInas/SEISbio_conda_env_backups/tmp"
SCP_OUTPUT_DIR = "ifc:/home/cperalta/py_conda_tests" # directory for tests
#SCP_OUTPUT_DIR = "drone_pi:/home/pi/SEISbio_conda_env_backups/tmp/" # scp based remote backup, requires ssh keys on remote server, optional.

# Get date and host info for definitive output dir
host_id = socket.gethostname()
backup_date = str(date.today()).replace("-","")

# Create output directory
out_dir = OUTPUT_DIR +"/conda_backup_" + backup_date + "/" + host_id + "_" + backup_date

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

# Get environments paths and names for yml creation
env =subprocess.Popen(["conda","info" ,"-e"], stdout=subprocess.PIPE)
out, err = env.communicate() # no se que estoy haciendo aqui pero funciona
env = out.decode()
env = env.replace('*','')

env = env[env.rfind('#')+1:].split() # to backup all env
#env = env[env.find('base'):].split() # to backup main conda installation environments only
#env = env[env.rfind('#')+1:env.find('base')-1].split() # to backup user env only

env_path= env[1:len(env):2]
env_yml= env[0:len(env):2]
env_yml= [out_dir + "/" + s + ".yml" for s in env_yml]


