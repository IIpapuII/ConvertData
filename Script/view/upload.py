from flask import Blueprint, render_template, request, redirect, url_for
from ..controller.extracData import verData, procesarDataDos, verDataDos
from ..controller.savaData import savefolder
from ..models.medidas import Save_Data_db

upload_file = Blueprint('upload_file', __name__)

@upload_file.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)

        if file:
            data_line = verDataDos(file)
            print(data_line)
            data = procesarDataDos(data_line)
            Save_Data_db(data)
            excel_file = savefolder(data)
            
            return render_template('success.html', excel_file=excel_file)

    return render_template('upload.html')
