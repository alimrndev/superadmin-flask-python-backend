from app import app
from app.controller import DosenController, MahasiswaController

@app.route('/')
def index():
    return 'Welcome to Python Backend App'

@app.route('/dosen', methods=['GET'])
def dosens():
    return DosenController.index()

@app.route('/mahasiswa', methods=['GET'])
def mahasiswas():
    return MahasiswaController.index()
