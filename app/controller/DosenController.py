from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa

from app import response, db, app
from flask import request, jsonify

import math

def read():
    try:
        dosen = Dosen.query.all()
        data = formatArray(dosen)
        return response.success(data, "success")
    except Exception as e:
        print(e)
        return response.internalServerError()

def formatArray(datas):
    array = []

    for i in datas:
        array.append(singleObject(i))

    return array

def singleObject(data):
    data = {
        'id' : data.id,
        'nidn' : data.nidn,
        'nama' : data.nama,
        'phone' : data.phone,
        'alamat' : data.alamat,
    }

    return data

def readDetail(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        mahasiswa = Mahasiswa.query.filter((Mahasiswa.dosen_satu == id) | (Mahasiswa.dosen_dua == id))

        if not dosen:
            return response.badRequest([], 'Tidak ada data dosen')
        
        dataMahasiswa = formatMahasiswa(mahasiswa)

        data = singleDetailMahasiswa(dosen, dataMahasiswa)

        return response.success(data, "success")
    
    except Exception as e:
        print(e)
        return response.internalServerError()

def singleDetailMahasiswa(dosen, mahasiswa):
    data = {
        'id': dosen.id,
        'nidn': dosen.nidn,
        'nama': dosen.nama,
        'phone': dosen.phone,
        'mahasiswa': mahasiswa,
    }

    return data

def singleMahasiswa(mahasiswa):
    data = {
        'id': mahasiswa.id,
        'nim': mahasiswa.nim,
        'nama': mahasiswa.nama,
        'phone': mahasiswa.phone,
    }

    return data

def formatMahasiswa(data):
    array = []
    for i in data:
        array.append(singleMahasiswa(i))
    
    return array

def create():
    try:
        data = request.form

        nidn  = data['nidn'].strip()
        nama  = data['nama'].strip()
        phone  = data['phone'].strip()
        alamat  = data['alamat'].strip()

        isExist = Dosen.query.filter(Dosen.nidn == nidn).first()
        if isExist is not None:
            return response.badRequest([], f"Data nidn {isExist.nidn} already exist!")

        dosens = Dosen(nidn=nidn, nama=nama, phone=phone, alamat=alamat)
        db.session.add(dosens)
        db.session.commit()
        
        return response.success("", "Sukses Menambahkan Data Dosen!")
    except Exception as e:
        print(e)
        return response.internalServerError()

def update(id):
    try:
        dosen = Dosen.query.get(id)
        if not dosen:
            return response.badRequest([], f"Dosen dengan id {id} tidak ditemukan!")
        
        dataPrev = {
            "nidn": dosen.nidn,
            "nama": dosen.nama,
            "phone": dosen.phone,
            "alamat": dosen.alamat,
        }

        dataUpdate = {}
        for key in ('nidn', 'nama', 'phone', 'alamat'):
            value = request.form.get(key)
            if value and value != "":
                dataUpdate[key] = value
                setattr(dosen, key, value)
        
        if not dataUpdate:
            return response.badRequest([], "Tidak ada data yang diubah!")

        db.session.commit()

        data = [
            {
                "prev": dataPrev,
                "update": dataUpdate,
            }
        ]

        db.session.commit()

        return response.success(data, 'Sukses Update data!')

    except Exception as e:
        print(e)
        return response.internalServerError()

def delete(id):
    try:
        dosen = Dosen.query.get(id)
        if not dosen:
            return response.badRequest([], f"Dosen dengan id {id} tidak ditemukan!")
        
        db.session.delete(dosen)
        db.session.commit()

        return response.success("", f"Berhasil Hapus Data!")
    except Exception as e:
        print(e)
        return response.internalServerError()

def get_pagination(clss, url, start, limit):
    # ambil data select
    results = clss.query.all()
    # ubah format
    data = formatArray(results)
    # hitung jumlah data
    count = len(data)

    obj = {}

    if count < start:
        obj['success'] = False
        obj['message'] = "Page yang dipilih melewati batas total data!"
        return obj
    else:
        obj['success'] = True
        obj['start_page'] = start
        obj['per_page'] = limit
        obj['total_data'] = count
        obj['total_page'] = math.ceil(count/limit)

        #previouss link
        if start == 1:
            obj['previous'] = ''
        else:
            start_copy = max(1, start-limit)
            limit_copy = start - 1
            obj['previous'] = f"{url}?start={start_copy}&limit={limit_copy}"

        #next link
        if start + limit > count:
            obj['next'] = ''
        else:
            start_copy = start + limit
            obj['next'] = f"{url}?start={start_copy}&limit={limit}"

        obj['results'] = data[(start - 1): (start - 1 + limit)]
        return obj
    
def paginate():
    start = request.args.get('start')
    limit = request.args.get('limit')
    baseUrl = app.config['BASE_URL']

    try:
        if start == None or limit == None:
            return jsonify(get_pagination(
                Dosen,
                f'{baseUrl}/api/dosen/page',
                start = request.args.get('start', 1),
                limit = request.args.get('limit', 3),
            ))
        else:
            return jsonify(get_pagination(
                Dosen,
                f'{baseUrl}/api/dosen/page',
                start = int(start),
                limit = int(limit),
            ))

    except Exception as e:
        print(e)
        return response.internalServerError()