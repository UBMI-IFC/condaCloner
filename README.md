# condaCloner

Por ahora es un script de R que crea los documentos YAML de los ambientes de anaconda en una maquina en particular
diseñado para trabajar con los servidores del IFC. 

Por ahora crea una carpeta local con la fecha del respaldo en el directorio **home** del usuario que ejecuta el script y
lo envia con **scp** a una carpeta en el directorio **home** del usuario en **UBMIPortal**


## Requerimientos

R

Rscript

llaves ssh de los servidores hacia UBMIPORTAL (Temporal)


## Ejecucion

$ Rscript condaCloner.R 
