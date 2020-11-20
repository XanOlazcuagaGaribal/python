# TP Docker & Flask :

## Comprendre la différence entre images et containers

Un conteneur Docker est une instance exécutable d’une image. 

## A quoi sert un ```Dockerfile```

Les Dockerfiles sont des fichiers qui permettent de construire une image Docker adaptée à nos besoins, étape par étape. Il permet de faire un fichier de configuration d'une image personnalisé.

## CheatSheet 

* **docker ```build```**: Permet de construire une image depuis un Dockerfile et un "context".

* **docker ```run```**: Permet de crée une couche de conteneur inscriptible sur l'image specifiée, puis la démarre.

* **docker ```exec```**: Permet de lancer une commande dans un conteneur en cours d'éxécution.

* **Port dans un container** : Lorsque que je vais lancer un serveur web comme nginx par exemple, il va rendre les pages web sur le port 80, mais seulement à l’intérieur du conteneur. Je n’y aurais pas accès car c’est totalement isolé, le conteneur a son propre réseau. Afin de pouvoir accéder aux pages web, je vais utiliser l’option -p qui va me permettre de spécifier le port de ma machine et lui dire vers quel port du conteneur je veux faire la liaison. De cette façon, je vais pouvoir accéder aux pages web via mon navigateur.

## Commandes éxécutés 

### Lancement du container getting-started

``` bash
docker run -d -p 80:80 docker/getting-started
```

Télécharge et lance le container tutorial de Docker

### Lancement du container *Hello World* 

``` bash
docker run hello-world
```

Télécharge et lance le container Hello World.

### Lancement du container ubuntu bash

``` bash
docker run -it ubuntu bash
```

Télécharge et lance le container de l'image ubuntu en bash. Après le lancement de la commande, une interface de commande ubuntu se lance.

### Liste des containers docker installés

``` bash
docker ps -a
```

La commande ```docker ps -a``` affiche la liste des containers dans docker.

ici on a :
* docker/getting-started
* hello-world
* ubuntu


### Liste des containers docker en cours d'éxécutions

``` bash
docker ps 
```
La commande ```docker ps``` affiche la liste des containers éxécutés.

ici on a : 
* docker/getting-started
* ubuntu

### Lance un container applicatif en python avec docker

``` bash
docker run -it --name python bitnami/python
```

Télécharge et lance un container python présent sur le hub docker.

Après téléchargement et installation, une interface de commande python s'éxécute.
