import os
import csv

# Punto 1: Listar los archivos en la carpeta
carpeta = "/ruta/a/tu/carpeta"
for archivo in os.listdir(carpeta):
    ruta_completa = os.path.join(carpeta, archivo)
    if os.path.isfile(ruta_completa):
        nombre_archivo, extension = os.path.splitext(archivo)
        print(f"Nombre: {nombre_archivo}, Extensión: {extension}, Ruta: {ruta_completa}")

# Punto 2: Leer el archivo Usuarios.csv
archivo_csv = 'Usuarios.csv'
with open(archivo_csv, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    # Punto 3: Imprimir columnas específicas
    for fila in csv_reader:
        nombres = fila.get('Nombres', 'No disponible')
        apellidos = fila.get('Apellidos', 'No disponible')
        dependencia = fila.get('Dependencia', 'No disponible')
        estado = fila.get('Estado', 'No disponible')
        total_columnas = len(fila)
        print(f"Nombres: {nombres}, Apellidos: {apellidos}, Dependencia: {dependencia}, Estado: {estado}, Total de columnas: {total_columnas}")

# Lineamientos de los archivos Programación.xml y Servicios.json
# Ver la estructura XML y JSON en los ejemplos anteriores.


