# Super Admin - Python - Flask - Backend
API Backend using Framework Flask Python

# Installer
<!-- Install Virtual Env  -->
- pip3 install virtualenv
<!-- Install Requerement.txt -->
- pip3 install -r requirements.txt

# Command
<!-- Copy Paste .env file  -->
- cp example.env .env

<!-- Create Virtual Env  -->
- virtualenv env
<!-- Activate Virtual Env on Windows -->
- . env\Scripts\activate
or
- source env/bin/activate
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
