import pandas as pd
from datetime import datetime, timedelta
import os
from werkzeug.datastructures import FileStorage

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
def verDataDos(file):
    try:
        if not isinstance(file, FileStorage):
            raise TypeError("Se esperaba un objeto FileStorage.")

        contenido = []
        for line in file:
            contenido.append(line.decode('utf-8').strip())

        if not contenido:
            raise ValueError("El archivo está vacío.")

        return contenido
    except TypeError as e:
        print(f"Error: {str(e)}") 
        return []  # Devolver una lista vacía en caso de tipo incorrecto
    except ValueError as e:
        print(f"Error: {str(e)}") 
        return []  # Devolver una lista vacía en caso de archivo vacío
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")
        return []  # Devolver una lista vacía en caso de otro tipo de error

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
            fecha = datetime.strptime(elementos[1][1:12], "%y%m%d%H%M%S")
            ingre = ingre+1
            continue
        hora = int(tiempo_muestreo_old) // 60
        if hora > 24:
            fecha += timedelta(days=1)
        minutos = int(tiempo_muestreo_old) % 60
        count = count+1
        data['No'].append(count)
        data['Fecha'].append(fecha.strftime("%m/%d/%y") + f' {hora}:{minutos:02d}')
        data['Cabezote Var 1'].append(float(elementos[1]))
        data['Cabezote Var 2'].append(float(elementos[2]))
        data['Cabezote Var 3'].append(float(elementos[3]))
        data['Cabezote Var 4'].append(float(elementos[4]))
        tiempo_muestreo_old = tiempo_muestreo_old + tiempo_muestreo
    print(ingre)
    return pd.DataFrame(data, columns=['No', 'Fecha','Cabezote Var 1', 'Cabezote Var 2', 'Cabezote Var 3', 'Cabezote Var 4'])

def procesarDataDos(data_int):
    line_count = len(data_int)
    print(f'Cantidad de Registro trabajar: {line_count}')
    result = []
    Result = []
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
    count_maxter = 0
    ingre = 0
    tiempo_muestreo_old = 0
    state = False
    for linea in data_int:
        count_maxter += 1
        lin = linea.replace(')','')
        lin = lin.replace(' ','')
        elementos = lin.split('(')
        if linea.strip().startswith('P'):
            if state == True:
                df = pd.DataFrame(data, columns=['No', 'Fecha','Cabezote Var 1', 'Cabezote Var 2', 'Cabezote Var 3', 'Cabezote Var 4'])
                result.append(df)
                print("Se Agrego Nuevo Registro")
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
            date_muestra = elementos[1][1:12]
            fecha = datetime.strptime(str(date_muestra), "%y%m%d%H%M%S")
            ingre = ingre + 1
            tiempo_muestreo_old = (int(fecha.hour)*60) + int(fecha.minute)
            print(fecha)
            continue
        hora = int(tiempo_muestreo_old) // 60
        if hora == 24 and minutos == 0:
            fecha += timedelta(days=1)
            tiempo_muestreo_old = 0
        minutos = int(tiempo_muestreo_old) % 60
        count = count+1
        data['No'].append(count)
        data['Fecha'].append(fecha.strftime("%m/%d/%y") + f' {hora}:{minutos:02d}')
        data['Cabezote Var 1'].append(float(elementos[1]))
        data['Cabezote Var 2'].append(float(elementos[2]))
        data['Cabezote Var 3'].append(float(elementos[3]))
        data['Cabezote Var 4'].append(float(elementos[4]))
        tiempo_muestreo_old = tiempo_muestreo_old + tiempo_muestreo
        if count_maxter == line_count:
            df = pd.DataFrame(data, columns=['No', 'Fecha','Cabezote Var 1', 'Cabezote Var 2', 'Cabezote Var 3', 'Cabezote Var 4'])
            result.append(df)
            print("Final Register")
        state = True
    return result
#Funcion encargada del guardar el archivo.
def saveResult(data_frame):
    df = data_frame
    file_path = os.path.join('static', 'output.xlsx')  # Ruta y nombre del archivo a guardar
    df.to_excel(file_path, index=False)

    absolute_path = os.path.abspath(file_path)  # Ruta absoluta del archivo guardado
    print(f"El archivo se guardó en: {absolute_path}")


#Lector de sql
def read_sql(name_file):
    with open(os.path.join('Script/static',name_file)) as file:
        sql_script = file.read()
        return sql_script