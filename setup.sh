#! /bin/bash

#Esse script deve ser executado com SUDO

#Instalando o Django 1.3.1
apt-get install python-dev python-setuptools build-essential python-pip
easy_install pip
pip install django==1.3.1

#Instalando o POSTGRE 8.4
apt-get install postgresql-8.4
apt-get install python-pgsql

#Configurando o Sistema do Ditex
chmod 777 /opt
mkdir /opt/TA1
cp -a . /opt/TA1
sudo -u postgres createdb BancoDitex
python /opt/TA1/manage.py syncdb
