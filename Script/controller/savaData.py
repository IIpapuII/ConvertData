import pandas as pd
from xlsxwriter import Workbook
import os

def savefolder(frame_data):
    nameFile = 'data.xlsx'
    excel_filename = os.path.join('Script/static', nameFile)
    writer = pd.ExcelWriter(excel_filename, engine='xlsxwriter')  # Ruta y nombre del archivo a guardar
    for idx, df in enumerate(frame_data, start=1):
        df.to_excel(writer, sheet_name=f'Hoja{idx}', index=False)
    
    writer._save()
    return nameFile

def saveResult(frame_data):
    nameFile = 'data_result.xlsx'
    excel_filename = os.path.join('Script/static', nameFile)
    df = pd.DataFrame(frame_data)
    df.to_excel(excel_filename, index=False)
    return nameFile