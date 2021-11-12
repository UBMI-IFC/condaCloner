# condaCloner

Script de R que crea los documentos YAML de los ambientes de anaconda en una maquina en particular diseñado para trabajar con los servidores del IFC. 

Por ahora crea una carpeta local con la fecha del respaldo en el NAS de la UBMI y lo envia con scp a una carpeta en el home de ubmi-drone 


## Requerimientos

R

Rscript

llaves ssh de los servidores hacia ubmi-drone (usuario pi)


## Ejecucion

$ Rscript condaCloner.R 
