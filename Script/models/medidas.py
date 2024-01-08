
from ..db.dbconect import get_db, close_db
import pandas as pd
import uuid
cursor= get_db()
insert_query = """
    INSERT INTO DataElectric (fecha_guardado, Fecha, CVar1, CVar2, CVar3, CVar4, CodeStatus)
    VALUES (CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?)
    """
def generate_unique_key(prefix='p1'):
    unique_id = uuid.uuid4().hex[:10]  # Genera un identificador único de 10 caracteres
    return f"{prefix}-{unique_id}"


def Save_Data_db(result_data):
    
    for entry in range(len(result_data)):
        token_key = generate_unique_key()
        print(token_key)
        df = pd.DataFrame(result_data[entry])
        
        for index, row in df.iterrows():
            Fecha = row['Fecha']
            cvar1 = row['Cabezote Var 1']
            cvar2 = row['Cabezote Var 2']
            cvar3 = row['Cabezote Var 3']
            cvar4 = row['Cabezote Var 4']
                        # Verificar si el token_key ya existe en la base de datos
            cur = get_db().cursor()
            cur.execute("SELECT COUNT(*) FROM DataElectric WHERE CodeStatus = ?", (token_key,))
            existing_token_count = cur.fetchone()[0]
            
            if existing_token_count > 0:
                # Si el token_key existe, generar uno nuevo
                token_key = generate_unique_key()
                print(f"El token_key existía en la base de datos. Se ha generado uno nuevo: {token_key}")
                
            # Imprimir los valores de las columnas seleccionadas en cada fila
            data_to_insert =(Fecha , cvar1 , cvar2 ,cvar3 ,cvar4 , token_key)
            # Ejecutar la consulta SQL
            cursor.execute(insert_query, data_to_insert)
        cursor.commit()
        print("Dato agreado.")

