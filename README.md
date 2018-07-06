# Eventex

Sistema de Eventos para aprendizado

[![Build Status](https://travis-ci.org/fobsorlando/eventex.svg?branch=master)](https://travis-ci.org/fobsorlando/eventex)]

[![Code Health](https://landscape.io/github/fobsorlando/eventex/master/landscape.svg?style=flat)](https://landscape.io/github/fobsorlando/eventex/master)

## Como desenvolver?

1. Clone o repositório;
2. Crie um virtualenv com Python 3;
3. Ative o virtualenv;
4. Instale as dependencias;
5. Configure a instancia com o .env;
6. Execute os testes.

''' console

git clone git@github....  wttd (ver depois como faz)
cd wttd
python3 -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test

'''
## Como fazer Deploy?

1. Crie uma instancia no Heroku;
2. Envie as configurações para o Heroku;
3. Define uma SECRET_KEY segura para instancia;
4. Defina DEBUG=False;
5. Configure o serviço de E-Mail;
6. Envie o codigo para o Heroku;

''' console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY='python contrig/secret_gen.py'
heroku config:set DEBUG=False
# Configure o e-mail
git push heorku master --force
'''


