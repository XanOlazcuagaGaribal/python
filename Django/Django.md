# Introduction framework Django - M1 Tech Lead


# Au programme
* Mercredi 2 décembre :
	* Présentation de Django
	* TP - réalisation d'un CMS
	
* Suivi
Créer un repository github **public** et faire a minima deux pushs par jour (matin : 11h30 & après midi : 16h30) afin que je vois ou vous en êtes.

# Ce que vous apprendrez dans ce cours
A la suite de ce cours vous pouvez:

 - Comprendre une architecture MVT (et MVC)
 - Construire une application Web avec Django

## Le framework [Django](https://www.djangoproject.com/)

### Pourquoi Django ?

 - C'est un framework qui permet de développer des applications web très
   rapidement
 - Django gère les couches bases (sécurité, cache, etc...) et
   permet aux développeurs de se focaliser sur l'application
  - Django est "scalable" qui est notamment utilisé sur des applications très
   utilisés (Spotify, Instagram, Pinterest, etc...)

### Avant de commencer, quelques recommandations

Il est préférable de travailler sur un système Unix (OS X, Ubuntu, ...) en dual boot ou en VM, plutôt que sur Windows. Car l’exécution de nombreuses lignes de commandes est plus simple sur Unix.

Un éditeur de texte, comme Atom, VisualCode (ou celui que vous préférez) pour éditer les fichiers.

### Le serveur Web Django
Django intègre par défaut son serveur web (fait en python), il permet au développeur de créer des applications rapidement sans devoir gérer la complexité d'un serveur Apache (au moins avant la mise en prod).

La commande permet de lancer un serveur web local :

    python manage.py runserver


On accède à l'application via http://127.0.0.1:8000/ (le port est paramétrable dans le fichier settings.py).

> Il n'est pas nécessaire de relancer le serveur si un changement de
> code est fait, il sera automatiquement pris en compte lors de sa
> sauvegarde. Toutefois, il faudra relancer le serveur pour l'ajout de
> nouveaux fichiers.

### Le projet vs l'application
Un **projet** Django c'est le point de départ, et c'est simplement un répertoire qui contient des fichiers de paramétrage et de gestion.
Dans un projet Django on trouve des **applications**, ce sont des briques indépendantes qui permettent la réalisation d'une ou plusieurs taches précise, exemple: gestion d'un blog, todo list, etc... 

> Il est possible de créer des applications directement dans le projet, ou au meme niveau que le projet. Toutefois, une bonne pratique est de définir nos applications au meme niveau que le projet pour permettre une réutilisation entre projets plus facile. 


### Les gestion des routes
Les requêtes HTTP se caractérisent par des **routes**: il s'agit du chemin permettant de structurer l'accessibilité des données.
- la route http://monserveur.com/list permet de lister des informations
- la route http://monserveur.com/edit/4 permet d'éditer une donnée en utilisant son ID
- la route http://monserveur.com/new permet de créer de nouvelles données

Notez qu'il est également possible développer une application Django implémentant une API REST [plus d'infos ici](https://www.django-rest-framework.org/).

## L'architecture MVT

Ce choix d'architecture permet de séparer les fonctionnalités.

### Le modèle
Le rôle du modèle est d'interagir avec la base de données. Les différentes requêtes pour aller chercher des items sont formatés pour être exploitable par l'application.
Dans Django, les modèles sont définis dans le fichier `models.py`de notre application.

### La vue
La vue a la responsabilité de recevoir la requête (via la route) et d'y répondre.
Dans Django, les vues de chaque application sont définies dans le fichier `views.py`.

### Le template
Un template est simplement un fichier HTML, qui en plus d'avoir les balises standard, contient du code pour des objets Python. Chaque fichier template est lié à une vue, les templates sont placées dans le dossier `templates` de l'application.

![MVT architecture](https://t1.daumcdn.net/cfile/tistory/99B782465BB8D0C61A)

## Ressources en + 

-   La documentation officielle de [Django en FR](https://docs.djangoproject.com/fr/3.1/) !

## TP : réalisation d'un CMS sous forme de Todo List


Il est temps de construire une application de type CMS (Content Management System), qui permettra de gérer une liste de tâches. Comme celle-ci :

![enter image description here](https://drive.google.com/uc?export=view&id=1Y_OlhvJH994EYELneRdjUvHpEoLy8y4w)
Cette application devra permettre de:
 - afficher la liste des taches sur la page d'accueil
 - ajouter des tâches dans la liste depuis la page d'accueil
 - éditer une tache (dans une vue dédiée)
 - dire que la tâche est réalisée (la barrer)
 - supprimer une tâche

### Quelques contraintes & recommendations

 1. Le nom du projet créé sera "TP_Django"
 2. Le nom de l'application sera "todo"
 3. le SGBD utilisé sera SQLite (nativement fourni avec Django)
 4. Le modèle implémenté dans la base de donnée sera le suivant:  ![enter image description here](https://drive.google.com/uc?export=view&id=1sH6lCxXPkt8cT54oIHYb9-7HIlEeBK2Z)
 5. Les sources à compléter, sont dispo ici: [Sources TP Django Todo List](https://drive.google.com/drive/folders/1fVmgHLogQgOqwrzcKUfv7yjPlJxruRa_?usp=sharing)
    * Les templates index et edit sont a déposer dans le dossier todo/templates/todo
    * le CSS, images (et JS pour ceux qui veulent) sont à déposer dans votre application dans le dossier todo/static/todo
	 

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU3NDc3NDM4NCwxODMwNjk2MDgxLC04Mz
kwNTkwOTMsNDAzNTE2ODY4LDE1MDg4NDA2NjEsNjQ2OTcxNzYx
LC0xNTI1MzAxOTkyLDUyNjc0NTMzNyw2NDM0MjQ3NDEsMzM2NT
U1ODg0LC0xMjYyMTA0OTUwLC0xNTA2NTA4MzUwLC0xODMxNDE1
Nzc3LDExMzIxODk0MTEsLTUyNTk4MjI4MywtMTAzOTE1NzA1OS
wtODgwNDQxNzA3LDExNDczNTg5MzgsMTY3NzgxNjM4NywxNTI2
MTg3MTgzXX0=
-->