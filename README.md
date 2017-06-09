#Projet python : sport dans le Pays de la Loire


### Récupération du projet via GitHub

A l'aide d'un terminal, récupérer les fichiers composant mon projet 
via github : 
````buildoutcfg
    git clone "https://github.com/asouphie/projet_python.git"
````

###Implémentation de la base de données

Ensuite, en vous placant dans le premier dossier du projet, c'est-à-
dire "projet_python" taper la commande suivante dans votre terminal : 
````buildoutcfg
    python3 datas.py
````

Cela va implémenter la base de données pour pouvoir la manipuler par 
la suite.

###Lancement du serveur

Avant de lancer votre serveur, il va d'abord falloir que vous téléchargiez
bottle.py, si vous ne l'avez pas déjà. Deux façons possible s'offre à vous : 
1. en temps que super utilisateur, dans un terminal, avec les requêtes
suivantes : (http://bottlepy.org/docs/dev/tutorial.html#installation)
````buildoutcfg
    sudo pip install bottle              
    sudo easy_install bottle             
    sudo apt-get install python-bottle
````

2. En téléchargeant directement le fichier bottle.py via le lien 
suivant : 
https://raw.githubusercontent.com/bottlepy/bottle/master/bottle.py


Dès lors que vous avez une base de données, il va falloir lancer le serveur
pour accéder au site. Pour cela veuillez taper la commande suivante : 
````buildoutcfg
    python3 server.py
````

Le serveur est lancé, il ne vous reste plus qu'à taper dans votre barre
de recherche de votre navigateur, l'url suivante : 
localhost:8080/index

Il n'y a plus qu'à utiliser l'application "Sport Pays de la Loire".