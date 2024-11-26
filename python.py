import os
import csv
import json
import xml.etree.ElementTree as ET

def listar_archivos(LARA):
    """
    Lista los archivos dentro de un directorio, identificando su nombre,
    extensión y ruta completa.

    :param directorio: Ruta del directorio a listar
    :type directorio: str
    :return: Lista de diccionarios con detalles de los archivos
    :rtype: list[dict]
    """
    archivos = []
    try:
        if not os.path.exists(directorio):
            print(f"El directorio '{directorio}' no existe.")
            return archivos

        for archivo in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, archivo)
            if os.path.isfile(ruta_completa):
                nombre, extension = os.path.splitext(archivo)
                archivos.append({
                    "Nombre": nombre,
                    "Extensión": extension,
                    "Ruta completa": ruta_completa
                })
    except Exception as e:
        print(f"Error al listar los archivos: {e}")
    
    return archivos

def leer_usuarios_csv(csv.DictReader):
    """
    Lee el contenido de un archivo CSV y extrae información específica.

    :param ruta_csv: Ruta al archivo CSV
    :type ruta_csv: str
    """
    try:
        with open(ruta_csv, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            print(f"\nInformación del archivo '{ruta_csv}':")
            for row in reader:
                print(f"Nombres: {row['Nombres']}, Apellidos: {row['Apellidos']}, "
                      f"Dependencia: {row['Dependencia']}, Estado: {row['Estado']}, "
                      f"Total de columnas: {len(row)}")
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")

def crear_programacion_xml(codigo.xml):
    """
    Crea un archivo XML de ejemplo con los lineamientos establecidos.

    :param ruta_xml: Ruta donde se guardará el archivo XML
    :type ruta_xml: str
    """
    try:
        root = ET.Element("Programacion")
        tarea = ET.SubElement(root, "Tarea")
        ET.SubElement(tarea, "ID").text = "001"
        ET.SubElement(tarea, "Nombre").text = "Desarrollo de módulo A"
        ET.SubElement(tarea, "Estado").text = "En progreso"

        tree = ET.ElementTree(root)
        tree.write(ruta_xml, encoding="utf-8", xml_declaration=True)
        print(f"\nArchivo XML '{ruta_xml}' creado exitosamente.")
    except Exception as e:
        print(f"Error al crear el archivo XML: {e}")

def crear_servicios_json(codigo.json):
    """
    Crea un archivo JSON de ejemplo con los lineamientos establecidos.

    :param ruta_json: Ruta donde se guardará el archivo JSON
    :type ruta_json: str
    """
    try:
        servicios = [
            {"ID": "101", "Nombre": "Hosting Web", "Estado": "Activo"},
            {"ID": "102", "Nombre": "Soporte Técnico", "Estado": "Pendiente"},
        ]
        with open(ruta_json, "w", encoding="utf-8") as file:
            json.dump(servicios, file, indent=4, ensure_ascii=False)
        print(f"\nArchivo JSON '{ruta_json}' creado exitosamente.")
    except Exception as e:
        print(f"Error al crear el archivo JSON: {e}")

if __name__ == "__main__":
    # Directorio a listar
    directorio = "./LARA"
    archivos = listar_archivos(directorio)
    print("\nArchivos encontrados en el directorio:")
    for archivo in archivos:
        print(f"Nombre: {archivo['Nombre']}, Extensión: {archivo['Extensión']}, Ruta: {archivo['Ruta completa']}")

    # Leer el contenido de Usuarios.csv
    ruta_csv = os.path.join(directorio, "Usuarios.csv")
    leer_usuarios_csv(ruta_csv)

    # Crear archivos XML y JSON
    ruta_xml = os.path.join(directorio, "CODIGO.xml")
    crear_programacion_xml(ruta_xml)

    ruta_json = os.path.join(directorio, "CODIGO.json")
    crear_servicios_json(ruta_json)
