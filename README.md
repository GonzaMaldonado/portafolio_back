Portafolio GM Backend
=======================

<!--
[![Lint](https://github.com/GonzaMaldonado/portafolio_front/actions/workflows/lint.yml/badge.svg?branch=master)](https://github.com/GonzaMaldonado/portafolio_front/actions/workflows/lint.yml?query=branch%3Amaster)
[![Tests](https://github.com/GonzaMaldonado/portafolio_front/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/GonzaMaldonado/portafolio_front/actions/workflows/test.yml?query=branch%3Amaster)
-->


## Description

CV, implementando autenticación y autorización de usuarios, los cúales tendrán acceso a páginas de Posts y Tasks.


Requirements
-----------

* Python: "3.11.2 o >"
* Pip: ""


Getting Started
-----------

- clone repo

    ```bash
    git clone https://github.com/GonzaMaldonado/portafolio_back.git
    ```

- create virtual enviroment (in this case I do it with virtualenv)

    ```bash
    virtualenv -p C:\Users\AppData\Local\Programs\Python\Python311\python.exe venv
    ```

- activate virtual enviroment

    ```bash
    venv\Scripts\activate
    ```

- install packages

    ```bash
    pip install -r requirements.txt
    ```

- do the migrations to the database

    ```bash
    python manage.py migrate
    ```

- run example project

    ```bash
    python manage.py runserver
    ```


- open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser


### Enviroment Variables
```
SECRET_KEY="secret_key_django"
SENDGRID_API_KEY="secret_key_sendgrid_for_sending_emails"
```


## Author

Gonzalo Maldonado
ex. [@GonzaMaldo](https://instagram.com/gonzamaldonado.06)
