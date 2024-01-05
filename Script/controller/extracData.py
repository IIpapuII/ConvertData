import pandas as pd
from datetime import datetime
import os

#Funcion encargada de leer los datos del archivo txt
def verData(path_home):
    try:
        with open(path_home, 'r') as archivo:
            contenido = archivo.readlines()
            if not contenido:  # Si el archivo está vacío
                print(ValueError("El archivo está vacío."))
                exit()
            return contenido
    except FileNotFoundError:
        print("El archivo no se encuentra.")
        exit()
    except ValueError as e:
        print(f"Error: {str(e)}") 
        exit()
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")
        exit()

#funcion encargada de procesar los datos al arreglo para la converción.
def procesarData(data_int):
    data = {
        'No': [],
        'Fecha': [],
        'Cabezote Var 1': [],
        'Cabezote Var 2': [],
        'Cabezote Var 3': [],
        'Cabezote Var 4': []
    }
    tiempo_muestreo = 0
    fecha = datetime
    count = 0
    ingre = 0
    tiempo_muestreo_old = 0
    for linea in data_int:
        lin = linea.replace(')','')
        lin = lin.replace(' ','')
        elementos = lin.split('(')
        if linea.strip().startswith('P'):
            tiempo_muestreo = 0
            tiempo_muestreo = int(elementos[3])
            fecha = datetime.strptime(elementos[1][1:12], "%y%m%d%H%M%S").strftime("%m/%d/%y")
            ingre = ingre+1
            continue
        hora = int(tiempo_muestreo_old) // 60
        minutos = int(tiempo_muestreo_old) % 60
        count = count+1
        data['No'].append(count)
        data['Fecha'].append(fecha + f' {hora}:{minutos:02d}')
        data['Cabezote Var 1'].append(float(elementos[1]))
        data['Cabezote Var 2'].append(float(elementos[2]))
        data['Cabezote Var 3'].append(float(elementos[3]))
        data['Cabezote Var 4'].append(float(elementos[4]))
        tiempo_muestreo_old = tiempo_muestreo_old + tiempo_muestreo
    print(ingre)
    return pd.DataFrame(data, columns=['No', 'Fecha','Cabezote Var 1', 'Cabezote Var 2', 'Cabezote Var 3', 'Cabezote Var 4'])

def procesarDataDos(data_int):
    result = []
    data = {
        'No': [],
        'Fecha': [],
        'Cabezote Var 1': [],
        'Cabezote Var 2': [],
        'Cabezote Var 3': [],
        'Cabezote Var 4': []
    }
    tiempo_muestreo = 0
    fecha = datetime
    count = 0
    ingre = 0
    tiempo_muestreo_old = 0
    for linea in data_int:
        lin = linea.replace(')','')
        lin = lin.replace(' ','')
        elementos = lin.split('(')
        if linea.strip().startswith('P'):
            df = pd.DataFrame(data, columns=['No', 'Fecha','Cabezote Var 1', 'Cabezote Var 2', 'Cabezote Var 3', 'Cabezote Var 4'])
            result.append(df)
            data = {
                    'No': [],
                    'Fecha': [],
                    'Cabezote Var 1': [],
                    'Cabezote Var 2': [],
                    'Cabezote Var 3': [],
                    'Cabezote Var 4': []
                }
            tiempo_muestreo = 0
            tiempo_muestreo = int(elementos[3])
            fecha = datetime.strptime(elementos[1][1:12], "%y%m%d%H%M%S").strftime("%m/%d/%y")
            ingre = ingre+1
            continue
        hora = int(tiempo_muestreo_old) // 60
        minutos = int(tiempo_muestreo_old) % 60
        count = count+1
        data['No'].append(count)
        data['Fecha'].append(fecha + f' {hora}:{minutos:02d}')
        data['Cabezote Var 1'].append(float(elementos[1]))
        data['Cabezote Var 2'].append(float(elementos[2]))
        data['Cabezote Var 3'].append(float(elementos[3]))
        data['Cabezote Var 4'].append(float(elementos[4]))
        tiempo_muestreo_old = tiempo_muestreo_old + tiempo_muestreo
    return result
#Funcion encargada del guardar el archivo.
def saveResult(data_frame):
    df = data_frame
    file_path = 'data.xlsx'  # Ruta y nombre del archivo a guardar
    df.to_excel(file_path, index=False)

    absolute_path = os.path.abspath(file_path)  # Ruta absoluta del archivo guardado
    print(f"El archivo se guardó en: {absolute_path}")
