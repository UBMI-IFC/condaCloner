# condaCloner

Python script to create a folder with anaconda environments backups as yml files.

Currently create updates of base and main conda installation environments, arguments to backup user environments and all anaconda environments to be included 

Creates: backup_folder/host_and_date_folder/yml_files

## Usage

$ python3 condaCloner.py 


## Notes

Command line arguments for : Output directory and backup options to be included

R script is fully functional but no longer maintained ; requires: __Rscript__ output directory must be specified into the script and optional remote backup via scp requires ssh-key authentication into remote machine.