# Conda environment cloner

library(stringr)

# Get environments paths and names
envs <- system("conda info -e", intern = T)[grepl("home", system("conda info -e", intern = T))]
envs <- str_replace(envs, "\\*", "")
envs <- gsub("\\s+", ",", envs)
envs <- read.table(text = envs, sep = ",")
colnames(envs) <- c("environment_yaml", "path")
envs$environment_yaml <- paste0(envs$environment_yaml,".yaml")

# Creates output directory for all and every backup
outdir <- paste0("/home/",
                 system("whoami", intern = T),
                 "/backupsConda")  # REPLACE WITH DEFINITVE DIRECTORY

outdir_final <- paste0(outdir,
                       "/",
                       system("hostname", intern = T),
                       "_",
                       system("date +%Y%m%d", intern = T))

ifelse(!dir.exists(outdir), dir.create(outdir), FALSE) # creates master backups directory if there is no one present
dir.create(outdir_final)

# YAML files creation
envs$environment_yaml <- paste0(outdir_final,"/",envs$environment_yaml)

cmmnd <- paste("conda env export -p",envs$path," >", envs$environment_yaml )

for( i in 1:length(cmmnd)){
  system(cmmnd[i],wait = T)
}

# Temporary fix until I can mount this on the NAS

system(paste("scp -r ", outdir_final ,"ifc:/home/cperalta/conda_backups_yaml"))
