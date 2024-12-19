
<h1  align="center"> plataforma back-end - EJECT </h1>

Este projeto consiste no desenvolvimento do back-end de uma API para uma plataforma de mídia social. O sistema é utilizado para gerenciar usuários, postagens, feeds e comentários, proporcionando funcionalidades típicas de uma plataforma social. O projeto foi desenvolvido como parte do treinamento e nivelamento dos trainees da Empresa Júnior da Escola de Ciências e Tecnologia da UFRN (EJECT).


## 🔧 Funcionalidades do Projeto

O sistema back-end oferece suporte às seguintes funcionalidades:

-  **Autenticação de Usuários:** Sistema de login, criação de contas e autenticação JWT (JSON Web Token).

-  **Gerenciamento de Postagens:** CRUD completo de postagens, com possibilidade de curtir e comentar.

-  **Feeds de Postagens:** Exibição de postagens em formato de feed, com suporte à paginação.

-  **Comentários:** CRUD de comentários em postagens.

-  **Administração:** Interface administrativa para gestão de usuários e conteúdos.

-  **Documentação da API:** A API é bem documentada com o Swagger para facilitar a integração com o front-end.


## 🚀 Tecnologias Utilizadas

O back-end foi construído utilizando as seguintes tecnologias:

-  **Django:** Framework principal para criação da aplicação web, gerenciamento de banco de dados e sistema de autenticação.

-  **Django REST Framework:** Utilizado para construir a API RESTful que comunica com o front-end.

-  **SQLite:** Banco de dados para armazenar informações dos usuários e conteúdo.

-  **Django Simple JWT:** Implementação de autenticação utilizando tokens JWT.

-  **Django Admin:** Para gerenciamento da plataforma diretamente pela interface administrativa.


## 📁 Estrutura do Projeto

A estrutura básica do projeto está organizada da seguinte forma:

    plataforma-backend/
    ├── plataformav/ # Diretório principal do app 
    ├── migrations/ # Migrações do banco de dados
    ├── init.py
    ├── admin.py # Configurações do admin do Django
    ├── apps.py
    ├── models.py # Modelos de dados (usuarios, postagens, comentários, etc.)
    ├── serializers.py # Serializadores da API
    ├── tests.py
    ├── views.py # Visões para a API
    ├── pagination.py # Configuração de paginação
    ├── manage.py # Script de gerenciamento do Django
    └── requirements.txt # Dependências do projeto

  
### Principais Modelos

-  **Account:** Modelo de usuário para armazenar dados de login e perfil.

-  **Post:** Modelo de postagem, que contém título, conteúdo e dados sobre o usuário que criou a postagem.

-  **PostFeed:** Modelo que contém o feed de postagens, exibido aos usuários.

-  **Comment:** Modelo de comentário, associado a postagens e usuários.
  

## 🛠 Como Rodar o Projeto

1. Clone o repositório:

`git clone https://github.com/VitorBurratto/plataforma-v-eject-back-end.git`

2. Entre no diretório:

`cd plataforma-v-eject-back-end`

3. Crie a venv:
  
`python -m venv ./venv`

`source venv/bin/activate`
  
4. Instale as dependências:

- Windows PowerShell:

`.\venv\Scripts\Activate.ps1`  

- Prompt de Comando (cmd):
  
`venv\Scripts\activate.bat`
  
- Git bash:
  
`source '/caminho/para/seu/pplataforma-v-eject-back-end/venv/Scripts/activate'`
  
5. Instale as dependências:

`pip install -r requirements.txt`
  
5. Aplique as migrações:
  
`python manage.py migrate`
  
6. Crie um superusuário:
  
`python manage.py createsuperuser`

7. Execute o servidor de desenvolvimento:

`python manage.py runserver`
  
8. Acesse o projeto:
  
`http://127.0.0.1:8000/`
  

## 🔑 Endpoints da API

Aqui estão as rotas principais da API:  

**- Account**

GET: http://127.0.0.1:8000/accounts/

Ação: Recuperar todas as contas de usuários.

POST: http://127.0.0.1:8000/accounts/

Ação: Criar uma nova conta (somente para superusuários ou administradores).

GET: http://127.0.0.1:8000/accounts/{account_id}/

Ação: Recuperar os detalhes de uma conta específica.

PUT: http://127.0.0.1:8000/accounts/{account_idd}/

Ação: Atualizar os dados de uma conta específica (somente o próprio usuário pode editar).

DELETE: http://127.0.0.1:8000/accounts/{account_id}/

Ação: Excluir uma conta específica (somente o próprio usuário pode excluir).

---

**- Post**

GET: http://127.0.0.1:8000/posts/

Ação: Recuperar todas as postagens.

POST: http://127.0.0.1:8000/posts/

Ação: Criar uma nova postagem.

GET: http://127.0.0.1:8000/posts/{posts_id}/

Ação: Recuperar os detalhes de uma postagem específica.

PUT: http://127.0.0.1:8000/posts{posts_id}/

Ação: Atualizar uma postagem específica (somente o autor pode editar sua respectva postagem).

DELETE: http://127.0.0.1:8000/posts/{posts_id}/

Ação: Excluir uma postagem específica (somente o autor pode excluir sua respectva postagem).

POST: http://127.0.0.1:8000/posts/{id}/like/

Ação: Adicionar um "like" à postagem especificada.

---

**- PostFeed**

GET: http://127.0.0.1:8000/postfeeds/

Ação: Recuperar todas as postagens do feed.

GET: http://127.0.0.1:8000/accounts/{account_id}/postfeeds/

Ação: Recuperar o feed de postagens de um usuário específico.

---

**- Comment**

GET: http://127.0.0.1:8000/comments/

Ação: Recuperar todos os comentários da plataforma.

POST: http://127.0.0.1:8000/comments/

Ação: Criar um novo comentário em uma postagem.

GET: http://127.0.0.1:8000/comments/{id}/

Ação: Recuperar os detalhes de um comentário específico.

PUT: http://127.0.0.1:8000/comments/{id}/

Ação: Atualizar um comentário específico (somente o autor pode editar).

DELETE: http://127.0.0.1:8000/comments/{id}/

Ação: Excluir um comentário específico (somente o autor pode excluir).

GET http://127.0.0.1:8000/comments/post/{post_id}/

Ação: Recupera todos os comentários de um post específico.

---

**- Autenticação**

POST: http://127.0.0.1:8000/token/

Ação: Gerar um token JWT para autenticação.  

POST: http://127.0.0.1:8000/token/refresh/

Ação: Atualizar o token JWT.


## ✔️ Testes

O projeto inclui testes unitários para verificar o funcionamentos correto das principais funcionalidades da API. Para rodar os testes, use o seguinte comando:
  
`python manage.py test`

- Autenticação de Usuários: Testes para verificar o registro de novos usuários, login e geração de tokens JWT.

- CRUD de Postagens: Testes para criação, edição, exclusão e recuperação de postagens.

- Comentários: Verificação da criação e edição de comentários em postagens.

- Paginação no Feed: Testes para garantir que a paginação funciona conforme esperado no endpoint do feed.

- Permissões: Testes para verificar se as ações de edição e exclusão são limitadas aos autores das postagens/comentários.


## 🧑‍💻Autores  

<img  src="https://github.com/VitorBurratto.png"  alt="Vítor Burratto"  width="100"  height="100"/> **[Vítor Burratto](https://github.com/VitorBurratto)**