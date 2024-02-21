# HelloFlask

## Installation et utilisation de Pyenv

- installation de pyenv et de ses dépendances

> sudo apt-get update; sudo apt-get install  make build-essential \  
> libssl-dev zlib1g-dev \  
> libbz2-dev libreadline-dev libsqlite3-dev \  
> wget curl llvm \  
> libncursesw5-dev \  
> xz-utils \  
> tk-dev \  
> libxml2-dev \  
> libxmlsec1-dev \  
> libffi-dev liblzma-dev   


> curl https://pyenv.run | bash  

message à la fin : demande de modification de fichiers pour lancer automatiquement pyenv et pas conda

- vérification du type de shell pour modification du fichier qui lance automatiquement conda/pyenv

https://www.baeldung.com/linux/interactive-non-interactive-login-non-login-shells

> echo $-  
himBHs  
> shopt login_shell  
login_shell    	off  

- modification du fichier ~/bashrc pour supprimer conda et ajouter pyenv 

> gedit ~/.bashrc

Dans le fichier, ajouter  :

'# Load pyenv automatically  
export PYENV_ROOT="$HOME/.pyenv"  
command -v pyenv >/dev/null || export  PATH="$PYENV_ROOT/bin:$PATH"  
eval "$(pyenv init -)"  
'# Load pyenv-virtualenv automatically  
eval "$(pyenv virtualenv-init -)"  

Et commenter entre :  

'# >>> conda initialize >>>
...
'# <<< conda initialize <<<


- check des versions de python / conda / autres disponibles avec pyenv

> pyenv install list

- installation de versions python/conda

> pyenv install VERSION

- check des env virtuels présents

> pyenv virtualenvs

- création et load d'un env virtuel 

> pyenv virtualenv VERSION NOMENV

> pyenv activate NOMENV

> pyenv deactivate

- installation dans l'env virtuel 

> pyenv activate NOMENV

Si juste python : 

> pip install PACKAGE


Si conda : 

> conda install PACKAGE 

- set de la version par défaut et local

> pyenv python --version

Rien par défaut au début sinon version

> pyenv global VERSION

ou 

> cd CHEMINDOSSIER

> pyenv local VERSION

## Installation et utilisation de Poetry

### Installation 

- on sort de tout environnement, le global c'est celui qu'on a configuré dans PyEnv

> pyenv deactivate

- installation de pipx (https://github.com/pypa/pipx)

> sudo apt install pipx

> pipx ensurepath

- installation de poetry  (https://python-poetry.org/docs/)

> pipx install poetry

> pipx upgrade poetry

- vérification installation

> poetry --version

- utiliser par défaut l'environnement virtuel python s'il y a 

> poetry config virtualenvs.prefer-active-python true

### Utilisation 

#### Dans un nouveau projet 

- se placer dans le dossier qui va contenir le nouveau dossier PROJET

> cd REPERTOIRE 

- creation du projet 

> poetry new PROJET 

- création des fichiers à l'intérieur 

> cd PROJET

> touch projet/nouveauscript.py 



#### Dans un projet existant 

- se placer dans le répertoire du projet PROJET

> cd PROJET

- activer un env virtuel pyenv OU créer un fichier .python-version (cf ci-dessus) pour que poetry sache de quelle version on parle

- initialiser poetry

> poetry init --no-interaction

#### Ajouter / updater/ supprimer des packages 

> poetry add PACKAGE 

> poetry update PACKAGE 

> poetry remove PACKAGE 

pour une version spécifique on peut la donner avec PACKAGE==VERSION et upgrade ne marchera plus

#### Créer un alias pour un script 

- modifier le fichier pyproject.toml en ajoutant le nom du script 'dossierscript/monscript.py'

> [tool.poetry.scripts] 

> alias = "dossierscript.monscript:main"

- mettre à jour poetry 

> poetry install

- utilisation de l'alias 

> poetry run ALIAS ARGUMENTS

#### Export pour réutilisation de l'application

-création des fichiers .whl et archive du répertoire courant 

> poetry build

#### Se placer dans l'env virtuel correspondant aux infos de poetry

- d'abord désactiver l'env courant et reboot le terminal 

> poetry shell

- ensuite on est dans l'environnement 

## helloFlask

### Description du projet

Création d'un site internet avec trois pages : index(=home), à propos de nous (= about) et contactez nous (=form). L'utilisateur voit ses réponses au formulaire dans une page supplémentaire 'Merci de nous avoir contacté "nom de la personne" !'(=result).

### Contributions au projet

#### Environnement

- installation de pyenv, poetry nécessaires, git optionnelle 

- cloner le repo avec git 

> git clone git@github.com:LexouLam/HelloFlask.git

- se placer dans le répertoire ./HelloFlask puis lancer poetry et activer l'environnement

> poetry install

> poetry shell

vérification que l'environnement et les packages sont bien chargés : 

> python ./helloflask/helloflaskscript.py

doit afficher :

>\* Serving Flask app 'helloflaskscript'  
\* Debug mode: off  
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.  
\* Running on http://127.0.0.1:5000  
Press CTRL+C to quit  

#### Modifications de l'app

- structure

├── helloflask  
│   ├── helloflaskscript.py  
│   └── templates  
│       ├── about.html  
│       ├── form.html  
│       ├── index.html  
│       └── result.html  
├── poetry.lock  
├── pyproject.toml  
└── README.md  

- helloflask : dossier de la première app

- helloflaskscript.py : script de l'app, avec flask

- helloflask/templates : fichiers html gérés par jinja2 pour l'affichage de l'app

Pour ajouter des fonctionnalités / pages, il faut à la fois ajouter une 'route' dans le script et créer un template 

