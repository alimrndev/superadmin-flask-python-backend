from app import app, response
from app.controller import UserController, DosenController, MahasiswaController, UploadController
from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required

@app.route('/')
def index():
    return 'Welcome to Python Backend App'

@app.route('/protected', methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return response.success(current_user, "Protected Success!")

@app.route('/create-admin', methods=['POST'])
def admins():
    return UserController.createAdmin()

@app.route('/login', methods=['POST'])
def logins():
    return UserController.login()

@app.route('/dosen', methods=['GET', 'POST'])
def dosens():
    if request.method == 'GET':
        return DosenController.read()
    elif request.method == 'POST':
        return DosenController.create()

@app.route('/dosen/<id>', methods=['GET', 'PUT', 'DELETE'])
def dosensDetail(id):
    if request.method == 'GET':
        return DosenController.readDetail(id)
    elif request.method == 'PUT':
        return DosenController.update(id)
    elif request.method == 'DELETE':
        return DosenController.delete(id)

@app.route('/mahasiswa', methods=['GET'])
def mahasiswas():
    return MahasiswaController.index()

@app.route('/file-upload', methods=['POST'])
def uploads():
    return UploadController.upload()