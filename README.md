
<h1  align="center"> plataforma back-end - EJECT </h1>

Este projeto consiste no desenvolvimento do back-end de uma API para uma plataforma de mídia social. O sistema é utilizado para gerenciar usuários, postagens, feeds e comentários, proporcionando funcionalidades típicas de uma plataforma social. O projeto foi desenvolvido como parte do treinamento e nivelamento dos trainees da Empresa Júnior da Escola de Ciências e Tecnologia da UFRN (EJECT).


## 🔧 Funcionalidades do Projeto

O sistema back-end oferece suporte as seguintes funcionalidades:

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

    plataforma-v-eject-back-end/
    ├── plataformav/ # Diretório principal do app 
    ├── migrations/
    ├── tests/
    ├── init.py
    ├── admin.py
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
  
`source '/caminho/para/seu/plataforma-v-eject-back-end/venv/Scripts/activate'`
  
5. Instale as dependências:

`pip install -r requirements.txt`
  
6. Crie as migrações:

`python manage.py makemigrations`

7. Aplique as migrações:
  
`python manage.py migrate`
  
8. Crie um superusuário:
  
`python manage.py createsuperuser`

9. Execute o servidor de desenvolvimento:

`python manage.py runserver`
  
10. Acesse o projeto:
  
`http://127.0.0.1:8000/`
  

## 🔑 Endpoints da API

Aqui estão as rotas principais da API:  

### **- Autenticação**

- `POST http://127.0.0.1:8000/token/`
  - Gerar um token JWT para autenticação.

- `POST http://127.0.0.1:8000/token/refresh/`
  - Atualizar o token JWT.

### **- Account**

- `GET http://127.0.0.1:8000/accounts/`
  - Recuperar todas as contas de usuários.

- `POST http://127.0.0.1:8000/accounts/`
  - Criar uma nova conta.

- `GET http://127.0.0.1:8000/accounts/{account_id}/`
  - Recuperar os detalhes de uma conta específica.

- `PUT http://127.0.0.1:8000/accounts/{account_id}/`
  - Atualizar os dados de uma conta específica (somente o próprio usuário pode editar).

- `DELETE http://127.0.0.1:8000/accounts/{account_id}/`
  - Excluir uma conta específica (somente o próprio usuário pode excluir).

### **- Post**

- `GET http://127.0.0.1:8000/posts/`
  - Recuperar todas as postagens.

- `POST http://127.0.0.1:8000/posts/`
  - Criar uma nova postagem.

- `GET http://127.0.0.1:8000/posts/{posts_id}/`
  - Recuperar os detalhes de uma postagem específica.

- `PUT http://127.0.0.1:8000/posts/{posts_id}/`
  - Atualizar uma postagem específica (somente o autor pode editar sua respectiva postagem).

- `DELETE http://127.0.0.1:8000/posts/{posts_id}/`
  - Excluir uma postagem específica (somente o autor pode excluir sua respectiva postagem).

- `POST http://127.0.0.1:8000/posts/{id}/like/`
  - Adicionar um "like" à postagem especificada.

### **- PostFeed**

- `GET http://127.0.0.1:8000/postfeeds/`
  - Recuperar todas as postagens do feed.

- `GET http://127.0.0.1:8000/accounts/{account_id}/postfeeds/`
  - Recuperar o feed de postagens de um usuário específico.

### **- Comment**

- `GET http://127.0.0.1:8000/comments/`
  - Recuperar todos os comentários da plataforma.

- `POST http://127.0.0.1:8000/commtens/{id}/`
  - Criar um novo comentário em uma postagem.

- `GET http://127.0.0.1:8000/comments/{id}/`
  - Recuperar os detalhes de um comentário específico.

- `PUT http://127.0.0.1:8000/comments/{id}/`
  - Atualizar um comentário específico (somente o autor pode editar).

- `DELETE http://127.0.0.1:8000/comments/{id}/`
  - Excluir um comentário específico (somente o autor pode excluir).


## ✔️ Testes

O projeto inclui testes unitários para verificar o funcionamentos correto das principais funcionalidades da API. Para rodar os testes, use o seguinte comando:
  
`python manage.py test`

**- Modelos:**

- Account: Verificação dos atributos adminUsername, password, name, email, cpf e cellphone.

- Post: Verificação dos atributos description e relação com o modelo Account.

- Like: Validação da relação entre o User e o Post.

- PostFeed: Verificação da relação entre o Account e o Post.

- Comment: Validação dos atributos post, account e content.

**-Serialização:**

- AccountSerializer: Verificação dos campos id, adminUsername, password, name, email, cpf, cellphone, dateBirth e user.

- PostSerializer: Verificação dos campos id, description, account, postType, image, code, likes e comments.

- PostFeedSerializer: Verificação dos campos id, account e post.

- CommentSerializer: Verificação dos campos id, post, account, content e createdAt.


## 🧑‍💻Autores  

<img  src="https://github.com/VitorBurratto.png"  alt="Vítor Burratto"  width="100"  height="100"/> **[Vítor Burratto](https://github.com/VitorBurratto)**
