#! /bin/bash

#Esse script deve ser executado com SUDO

#Instalando o Django 1.3.1
easy_instal pip
pip install django==1.3.1

#Instalando o POSTGRE 8.4
apt-get install postgresql-8.4
apt-get install python-pgsql

#Configurando o Sistema do Ditex
chmod 777 /opt
cp -a tpcavancados /opt
sudo -u postgres createdb BancoDitex
python /opt/tpcavancados/manage.py syncdb
