import pandas as pd
from xlsxwriter import Workbook

def savefolder(frame_data):
    writer = pd.ExcelWriter('data.xlsx', engine='xlsxwriter')  # Ruta y nombre del archivo a guardar
    for idx, df in enumerate(frame_data, start=1):
        df.to_excel(writer, sheet_name=f'Hoja{idx}', index=False)
    
    writer._save()