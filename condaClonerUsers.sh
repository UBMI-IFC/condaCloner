# crea respaldos desde una lista 
#TODO falta cambiar el path a uno relativo
source /home/anaconda/miniconda3/etc/profile.d/conda.sh

while read line; do
  conda activate $line
  myfile=$(echo $line | cut -f3,6 -d '/' | sed 's|/|_|')
  echo $myfile
  conda env export --no-builds | grep -v -e '^prefix'  >  $myfile.yml
  conda deactivate
done < $1
