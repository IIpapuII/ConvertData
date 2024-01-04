from .extracData import verData, procesarData, saveResult

'''
Elemento encargado del llamado de la visual de la información
y menu de la herramienta
'''

def setup():
    print('Ingrese la ruta del archivo a tratar: ')
    #path_document = str('D:/EDUCACION PLATZI/ConverDocument/Script/controller/archivo.txt' ) 
    path_document = input() 
    data_line = verData(path_document)
    data = procesarData(data_line)
    print(data)
    saveResult(data)
    
