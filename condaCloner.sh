source /home/anaconda/miniconda3/etc/profile.d/conda.sh

for line in $(conda env list | tr  -s ' ' ']' | cut -f 2 -d ] | grep -e '^/'); do
  conda activate $line
  myfile=$(echo $line | sed 's/.*\///')
  conda env export --no-builds | grep -v -e '^prefix'  >  $myfile.yml
  conda deactivate 
done

