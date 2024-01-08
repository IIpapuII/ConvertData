from flask import Blueprint, render_template, request, redirect, url_for
from ..db.dbconect import get_db, close_db
from ..controller.savaData import saveResult
import pandas as pd

query_data = Blueprint('query_data',__name__)
conn = get_db()
def get_filtered_data(fecha, code_status):
    
    query = "SELECT * FROM DataElectric WHERE Fecha like ? or CodeStatus = ?"
    filtered_data = pd.read_sql_query(query, conn, params=(f'%{fecha}%', code_status))
    
    return filtered_data

@query_data.route('/query',methods=['GET', 'POST'])
def queryData():
    return render_template('consult.html')

@query_data.route('/filter', methods=['POST'])
def filter_data():
    # Obtener los valores del formulario
    fecha = request.form['fecha']
    code_status = request.form['code_status']

    # Obtener los datos filtrados
    filtered_data = get_filtered_data(fecha, code_status)
    saveResult(filtered_data)
    # Mostrar los datos en una tabla en la plantilla
    return render_template('filtered_data.html', data=filtered_data)