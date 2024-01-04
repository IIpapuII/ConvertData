from .extracData import verData, procesarData, saveResult

'''
Elemento encargado del llamado de la visual de la información
y menu de la herramienta
'''

def setup():
    print('Ingrese la ruta del archivo a tratar: ')
    path_document = input()

    if not path_document:
        print('No se ingresó ninguna ruta. El proceso ha sido cancelado.')
        return
    
    data_line = verData(path_document)
    
    if isinstance(data_line, str):  # Manejar posibles mensajes de error
        print(data_line)
        return
    
    data = procesarData(data_line)
    print(data)
    saveResult(data)
    
