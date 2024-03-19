from app.model.mahasiswa import Mahasiswa

from app import response

def index():
    try:
        mahasiswa = Mahasiswa.query.all()
        data = formatArray(mahasiswa)
        return response.success(data, "success")
    except Exception as e:
        print(e)

def formatArray(datas):
    array = []

    for i in datas:
        array.append(singleObject(i))

    return array

def singleObject(data):
    data = {
        'id' : data.id,
        'nim' : data.nim,
        'nama' : data.nama,
        'prodi' : data.prodi,
        'alamat' : data.alamat,
        'phone' : data.phone,
        'dosen_satu' : data.dosen_satu,
        'dosen_dua' : data.dosen_dua,
    }

    return data
