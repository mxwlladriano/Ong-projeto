# SESMUS

Este projeto visa fazer a criação e gerenciamento de cadastros de uma ONG.

## Pré-requisitos

Antes de começar, você precisa ter instalado em sua máquina:

- Python >= 3.x
- pip (geralmente já vem instalado com o Python)

## Instalação

1. Clone este repositório:

```bash
git clone https://github.com/RafaelSoares12/ongProject.git
```

2. Acesse o diretório do projeto:

```bash
cd ongProject
```

3. Crie um ambiente virtual para isolar as dependências do projeto (O exemplo abaixo mostrar com venv do Python, mas podem ser outras, como Conda):

```bash
python -m venv venv
```

4. Ative o ambiente virtual:

No Windows:

```bash
venv\Scripts\activate
```

No macOS e Linux:

```bash
source venv/bin/activate
```

5. Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

6. Realize as migrações do banco de dados:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Executando o Projeto

Para criar o usuário inicial:

```bash
python manage.py createsuperuser
```

Para iniciar o servidor de desenvolvimento, execute o seguinte comando:

```bash
python manage.py runserver
```

O servidor estará acessível em [http://localhost:8000](http://localhost:8000).
