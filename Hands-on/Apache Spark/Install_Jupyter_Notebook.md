sudo apt-get update 

sudo apt install python3-pip

sudo -H pip3 install --upgrade pip 

sudo -H pip3 install virtualenv 

mkdir jupyter 

# move inside the directory 

cd jupyter 

virtualenv environment 

source environment/bin/activate 

# install Jupyter notebook 

pip install jupyter 

# open Jupyer notebook terminal 

jupyter notebook --ip=*

