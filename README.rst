P2 Tópicos Avançados 1
+++++++++++++++++++++++
Dupla: Fábio e Karolyne
_______________________

Instalando o Projeto
=====================
Executar pelo terminal o comando: $ sudo ./setup.sh

Durante a execução deverá ser criado um super usuário para o Django.

Será perguntado se deseja criar o super usuário, deve-se digitar "yes", digitar o usuário, email e senha.


Rodar o Projeto
================
Após a conclusão da instalação executar o comando: $ python /opt/TA1/manage.py runserver

A página inicial do sistema é http://localhost:8000/login

O sistema pode ser acessado com o usuario e senha cadastrados durante a instalação.


Serviços Oferecidos
====================
*Lista de Oportunidades Abertas*
================================
Requisitos:

Não tem

Retorna:

[{'empresa': int, 'descoportunidade': string, 'curso': int, 'tpoportunidade': String, 'vaga': String, 'dtfim': date, 'dtinicio': date, 'id': int, 'nrvagas': int}]


*Cadastrar Oportunidade*
========================
Requisitos:

[{'empresa': int, 'descoportunidade': string, 'curso': int, 'tpoportunidade': String, 'vaga': String, 'dtfim': date, 'dtinicio': date, 'id': int, 'nrvagas': int}]

Retorna:

Não tem


*Cadastrar Participante em Evento*
==================================
Requisitos:
[{'evento': int, 'participante': int}]

Retorna:

Não tem


