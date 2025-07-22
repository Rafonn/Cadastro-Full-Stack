# Sistema Cadastro de Produto

## Visão Geral

Este é um projeto full-stack. A aplicação consiste em um sistema de gerenciamento de catálogo de produtos (CRUD - Criar, Ler, Atualizar, Deletar) com autenticação de usuário.

O sistema foi construído com uma arquitetura desacoplada, com um backend em Flask que serve uma API RESTful e um frontend em Angular que consome essa API. A aplicação é totalmente containerizada com Docker para facilitar a implantação e garantir a consistência do ambiente.

## Funcionalidades Principais

  * **Autenticação de Usuário:** Sistema de login com usuário e senha.
  * **Proteção de Rotas:** Apenas usuários autenticados podem acessar a página de gerenciamento de produtos.
  * **CRUD de Produtos:**
      * Cadastro de novos produtos com nome, marca e valor.
      * Listagem de todos os produtos cadastrados em uma tabela.
      * Edição dos dados de um produto existente.
      * Exclusão de produtos.
  * **Logout:** Funcionalidade para encerrar a sessão do usuário.

## Tech Stack

  * **Backend:** Python, Flask, Gunicorn
  * **Frontend:** Angular, TypeScript
  * **Banco de Dados:** PostgreSQL
  * **Fila/Cache:** Redis
  * **Autenticação:** JWT (JSON Web Tokens)
  * **Containerização:** Docker

## IMPORTANTE

Para fazer o login na aplicação, utilize as seguintes credenciais fictícias:

  * **Usuário:** `admin`
  * **Senha:** `password123`

## Pré-requisitos

Antes de começar, garanta que você tem os seguintes softwares instalados:

  * Python 3.9+
  * Node.js 18+ e npm
  * Docker (opcional)

-----

## Configuração do Projeto

1.  **Clone o Repositório (se aplicável):**

    ```bash
    git clone https://github.com/Rafonn/Cadastro-Full-Stack.git
    cd Cadastro-Full-Stack
    ```

2.  **Crie e Ative um Ambiente Virtual Python (opcional):**
    Este passo é necessário apenas para rodar o backend localmente.

    ```bash
    # Navegue até a pasta do backend
    cd backend

    # Crie o ambiente virtual
    python -m venv venv

    # Ative o ambiente
    # No Windows:
    venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instale as Dependências Python:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Instale as Dependências do Frontend:**

    ```bash
    # Navegue até a pasta do frontend
    cd ../frontend

    # Instale os pacotes Node.js
    npm install
    ```

5.  **Configure as Variáveis de Ambiente:**
    Crie um arquivo .env na raiz do projeto:

    ```env
    SECRET_KEY='sua_chave_secreta'
    DATABASE_URL='postgresql://user:password@localhost:5432/sua_base_de_dados'
    REDIS_URL='redis://localhost:6379'
    ```

    Caso vá utilizar docker, adicione as seguintes variáveis nesse mesmo arquivo:

    ```env
    DB_USER=user
    DB_PASSWORD=password
    DB_NAME=sua_base_de_dados
    ```

-----

## Executando a Aplicação

A forma recomendada de executar a aplicação é com Docker Compose, pois ele gerencia todos os serviços (backend, frontend, banco de dados e Redis) automaticamente.

### Localmente

Se preferir rodar os serviços separadamente:

1.  **Inicie os Serviços no Docker:**
    Tenha um servidor redis rodando e um banco de dados postgreSQL criado.

    Opcional:
    Inicie o banco de dados e o Redis com o Docker Compose:
    ```bash
    docker-compose up -d postgres redis
    ```
2.  **Inicie o Backend Flask:**
    No terminal, na pasta `/backend` e com o ambiente virtual ativado:
    ```bash
    python run.py
    ```
3.  **Inicie o Frontend Angular:**
    Em um **novo terminal**, na pasta `/frontend`:
    ```bash
    ng serve
    ```
4.  **Acesse a Aplicação:**
    Abra seu navegador e acesse: **`http://localhost:4200`**

### Com Docker

**IMPORTANTE: No diretório /backend/run.py comente ou exclua a linha ```app.run(debug=True)```** 

Este comando irá construir as imagens e iniciar todos os contêineres de uma só vez.

1.  **Execute o Docker Compose:**
    Na raiz do projeto (onde está o `docker-compose.yml`), execute:
    ```bash
    docker-compose up --build
    ```
2.  **Acesse a Aplicação:**
    Abra seu navegador e acesse: **`http://localhost:4200`**

-----

## Como usar?

1.  Acesse `http://localhost:4200`. Você será redirecionado para a tela de login.
2.  Use as credenciais fornecidas na seção **IMPORTANTE**.
3.  Após o login, você verá a página de gestão de produtos, com um formulário para cadastro e uma tabela com os produtos existentes.
4.  Use o formulário para cadastrar novos produtos ou editar produtos existentes clicando no botão "Editar".
5.  Use o botão "Excluir" na tabela para remover um produto.
6.  Clique em "Logout" para encerrar a sessão e retornar à tela de login.

## Uso da API

O backend expõe os seguintes endpoints, protegidos por autenticação JWT:

  * `POST /api/auth/login`: Autentica o usuário e retorna um token.
  * `GET /api/products`: Retorna a lista de todos os produtos.
  * `POST /api/products`: Cria um novo produto.
  * `PUT /api/products/{id}`: Atualiza um produto existente.
  * `DELETE /api/products/{id}`: Deleta um produto.

## Estrutura dos produtos no postgreSQL

A tabela `products` no banco de dados tem a seguinte estrutura:

  * **`id`**: `SERIAL` (Integer, Auto-incremento, Chave Primária)
  * **`name`**: `VARCHAR(120)` (Texto, Não nulo)
  * **`brand`**: `VARCHAR(120)` (Texto, Não nulo)
  * **`value`**: `FLOAT` (Número de ponto flutuante, Não nulo)