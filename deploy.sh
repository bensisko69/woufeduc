# construction image -t pour le nom et . pour le chemin ou ce trouve le dockerfile
docker build -t bensisko/wouf-educ .
#  cree le conteneur qui lance le serveur
# --rm pour le supprimer a la fin de l'execution
# -it recuperer la sortie standard 
# -v $PWD:/app partage du dossier courant avec le conteneur
# -p exposition du port 9999 du conteneur vers le port 80 du host 
docker run --rm -it -v $PWD:/app -p 80:9999 bensisko/wouf-educ