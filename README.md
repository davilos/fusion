# Fusion v2
Este projeto é uma aplicação com Python e Django. Consiste em um site com registro/login de contas, 
apresentação de dados no index através do ORM. Também já vem embutido o /admin do próprio Django para o login de superusuários. Tudo isso dockerizado, legal, né? :D

O projeto ainda não está em produção, mas já pode ser testado. Você só precisa ter o Docker e o docker-compose instalado na sua máquina!

Se você já tem tudo que precisa, basta agora criar um arquivo .env na `RAIZ` do projeto. Eu criei um exemplo dele, basta você copiar e colar, OU retirar o "-example".

Não precisar mudar nenhum valor das variáveis, mas caso prefira, manda ver! :)

## Como rodar o projeto

Agora que já temos tudo definido, vamos começar a trabalhar com o docker-compose.
Primeiro de tudo, você terá que rodar o comando `make build`.
E por fim, o `make start`. Após esses comandos funcionarem, você já pode começar a testar o projeto!

## Como acessar o /admin

Para você preencher os dados necessários para serem mostrados no index, você precisa ser um superuser.
Para criar um, basta rodar o comando `make createsuperuser`, e então fornecer seus dados para cadastro.

Após isso, bastar acessar o `/admin` na URL, e fazer o login.
`http://0.0.0.0:8000/admin/`.

---
Nessa **v2**, eu dockerizei o Django e o banco de dados (PostgreSQL), para ficar mais fácil a inicialização do projeto, e ainda adicionei o Makefile para
diminuir a complexidade dos comandos digitados no terminal.

Em versões posteriores, pretendo adicionar APIs REST com o Django REST Framework!
