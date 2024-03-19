# Python-Backend
Backend use Python Language and Framework Flask

# Installer
<!-- Install Virtual Env  -->
- pip3 install virtualenv
<!-- Install Framework Flask  -->
- pip3 install flask
<!-- Install python-dotenv  -->
- pip3 install python-dotenv
<!-- Install flask-sqlalchemy -->
- pip3 install flask-sqlalchemy
<!-- Install flask-migrate -->
- pip3 install flask-migrate
<!-- Install pymysql -->
- pip3 install pymysql
<!-- Install werkzeug password hash -->
- pip3 install werkzeug
<!-- Install Flask JWT -->
- pip3 install flask-jwt-extended

# Command
<!-- Create Virtual Env  -->
- virtualenv env
<!-- Activate Virtual Env on Windows -->
- . env\Scripts\activate
<!-- Deactivate Virtual Env on Windows -->
- deactivate
<!-- Flask Run -->
- flask run
<!-- Flask Run Debug Mode On -->
- flask run --debug
<!-- Init pymysql -->
- flask db init
<!-- Migrate pymysql -->
- flask db migrate -m "comment"
<!-- Upgrade pymysql -->
- flask db upgrade
