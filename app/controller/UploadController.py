from app.model.image import Image

from app import response, app, db, upload_config
from flask import request
from werkzeug.utils import secure_filename

import os
import uuid

def upload():
    try:
        title = request.form.get("title")

        if 'file' not in request.files:
            return response.badRequest([], "File tidak tersedia!")
        
        file = request.files['file']

        if file.filename == '':
            return response.badRequest([], "File tidak tersedia!")
        if file and upload_config.allowed_file(file.filename):
            uid = uuid.uuid4()
            filename = secure_filename(file.filename)
            renamefile = f"Flask-{uid}-{filename}"

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], renamefile))

            uploads = Image(title=title, path_name=renamefile)
            db.session.add(uploads)
            db.session.commit()

            return response.success({
                "title": title,
                "path_name": renamefile,
            }, "Success Upload File!")
        else:
            return response.badRequest([], "File tidak diizinkan!")
    except Exception as e:
        print(e)
        return response.internalServerError()
