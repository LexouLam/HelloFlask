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