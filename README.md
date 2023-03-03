# Fusion
Este projeto é uma aplicação Django a qual eu ainda estou desenvolvendo e atualizando todos os dias.

No momento não fiz um deploy no projeto, mas você pode testá-lo na sua máquina.

Primeiro vamos ver as bibliotecas que você precisa ter instaladas na sua máquina. Lembrando que eu utilizo o Python ^3.11.

* Django
* psycopg2-binary
* gunicorn
* dj-static
* django-stdimage
* blue
* isort
* django-adminlte2
* dj-database-url
* whitenoise

Antes, temos que mudar o settings.py da pasta "fusion", pois ela está com configurações para o deploy.

## Altere todos os comandos a seguir
```
Debug = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_do_banco_de_dados',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

"""
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'), conn_max_age=600),
}
"""
```
E claro, para o banco de dados funcionar, você tem que baixar o Postgresql e configurá-lo na sua máquina.

## Como rodar o projeto

```
poetry shell
poetry install

python3.11 manage.py migrate
python3.11 manage.py runserver
```

OBS: Como ainda estou atualizando o projeto constantemente, podem surgir bibliotecas novas, que talvez não seja do seu interesse.
Por exemplo as bibliotecas que vou utilizar para testar todo o projeto.
