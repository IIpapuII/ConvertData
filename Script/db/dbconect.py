import sqlite3
from ..controller.extracData import read_sql
import threading

# Crear un objeto local para manejar la conexión en cada hilo
local = threading.local()
DATABASE= ("medidas.db")

def get_db():
    # Verificar si ya existe una conexión en el hilo actual
    if not hasattr(local, 'db'):
        # Si no hay conexión, crear una nueva para este hilo
        local.db = sqlite3.connect('medidas.db',check_same_thread=False)
        local.db.row_factory = sqlite3.Row
    
    return local.db

def close_db():
    # Verificar si hay una conexión en el hilo actual
    if hasattr(local, 'db'):
        # Cerrar la conexión si existe
        local.db.close()
        del local.db  # Eliminar la conexión para este hilo


def init_db():
    with sqlite3.connect(DATABASE, check_same_thread=False) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='movie'")
        table_exists = cursor.fetchone()
        if not table_exists:
           cursor.execute(read_sql('modelo.sql'))
        cursor.close()

def init_app():
    init_db()
    
close_db()


