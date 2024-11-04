import json

def cargar_datos():
    try:
        with open('gestion/gestion.json', 'r', encoding='utf-8') as archivo:
            campos = json.load(archivo)
            return [tuple(estudiante) for estudiante in campos.get("estudiantes", [])]
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def guardar_datos(lista):
    # Guardar la lista actualizada en el archivo
    with open('gestion/gestion.json', 'w', encoding='utf-8') as archivo:
        estudiantes_json = [list(estudiante) for estudiante in lista]
        json.dump({"estudiantes": estudiantes_json }, archivo, ensure_ascii=False, indent=4)
