sudo apt-get update 

sudo apt install python3-pip

sudo -H pip3 install --upgrade pip 

sudo -H pip3 install virtualenv 

mkdir jupter 

# move inside the directory 

cd jupyer 

virtualenv environment 

source environment/bin/activate 

# install Jupyter notebook 

pip install jupyter 

# open Jupyer notebook terminal 

jupyter notebook --ip=*

