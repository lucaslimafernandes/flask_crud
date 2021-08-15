# Flask_Crud
Desenvolvido por:
Lucas Lima Fernandes

## Instalação

1.  Criar um ambiente virtual (venv)
>python3 -m venv flaskEnv

2.  Ativar o venv
>source vEnv/bin/activate   #Linux

> source vEnv/Scripts\activate  #Windows

3.  Instalar os pacotes
>python -m pip install --upgrade pip

>pip install -r requirements.txt

4. Configurar o banco de dados
rodar o python

>python

>from project import db, create_app

>db.create_all(app=create_app())


5.  Rodar o Flask
>export FLASK_APP=main

>flask run

## Rodar
>export FLASK_APP=project

>export FLASK_DEBUG=1

>flask run


## Opções

1. home
2. signup
3. login
4. profile
5. edit
6. delete
7. logout


## requirements
flask
flask-sqlalchemy
flask-login

está configurado para usar SQlite
