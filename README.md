# Super Admin - Python - Flask - Backend
API Backend using Framework Flask Python

# Installer
<!-- Install Virtual Env  -->
- pip3 install virtualenv

<!-- Install Framework Flask  -->
- pip3 install flask
<!-- Install werkzeug password hash / utils -->
- pip3 install werkzeug

<!-- Install python-dotenv  -->
- pip3 install python-dotenv
<!-- Install Flask RESTful API -->
- pip3 install flask-restful
<!-- Install Flask JWT Auth -->
- pip3 install flask-jwt-extended

<!-- Install flask-sqlalchemy -->
- pip3 install flask-sqlalchemy
<!-- Install flask-migrate -->
- pip3 install flask-migrate
<!-- Install pymysql -->
- pip3 install pymysql

<!-- Install pytest -->
- pip3 install pytest
<!-- Install pytest-cov -->
- pip3 install pytest-cov

# Command
<!-- Copy Paste .env file  -->
- cp example.env .env

<!-- Create Virtual Env  -->
- virtualenv env
<!-- Activate Virtual Env on Windows -->
- . env\Scripts\activate
<!-- Deactivate Virtual Env on Windows -->
- deactivate

<!-- Init pymysql -->
- flask db init
<!-- Migrate pymysql -->
- flask db migrate -m "comment"
<!-- Upgrade pymysql -->
- flask db upgrade

<!-- Flask Run (Prod) -->
- flask run
<!-- Flask Run Debug Mode On (Dev or Stag) -->
- flask run --debug
