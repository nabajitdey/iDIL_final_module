install postgresql and pgadmin

make a database in the pgadmin server with the name of 'nlp_ice'

make a conda environment of python=3.6
e.g. conda create -n myenv python=3.6

activate the env

pip install -r requirements.txt

python manage.py runserver

python manage.py makemigrations

python manage.py migrate

conda install pytorch-cpu torchvision-cpu -c pytorch

