# Conda environment cloner

# Get environments paths and names
envs <- system("conda info -e", intern = T)[grepl("home", system("conda info -e", intern = T))]
envs <- read.table(text = gsub("\\s+", ",", gsub("\\*", "",envs)), sep = ",")
colnames(envs) <- c("environment", "path")

# Creates local  output directory for all and every backup
outdir <- paste0("/UBMInas/SEISbio_conda_env_backups/seisbio_",
                 system("date +%Y%m%d", intern = T)
                 )

outdir_final <- paste0(outdir,
                       "/",
                       system("hostname", intern = T),
                       "_",
                       system("date +%Y%m%d", intern = T))

ifelse(!dir.exists(outdir), dir.create(outdir), FALSE) # creates master backups directory if there is no one present
dir.create(outdir_final)

# YAML files creation
envs$environment_yaml <- paste0(outdir_final,"/",envs$environment,".yml")

envxport <- paste("conda env export -p",envs$path," >", envs$environment_yaml )
ymladapt <- paste0("sed -i  's/name: null/name: ", envs$environment,"/;$d' ", envs$environment_yaml )

for( i in 1:length(envxport)){
  system(envxport[i],wait = T)
  system(ymladapt[i],wait = T)
}

# Optional remote backup

system(paste("scp -r ", outdir_final ,"drone_pi:/home/pi/SEISbio_conda_env_backups/"))
