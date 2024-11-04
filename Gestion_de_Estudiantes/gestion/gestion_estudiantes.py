import json
import os
import pandas as pd
from gestion.gestion_cursos import CARRERAS

db_dir = os.path.join("gestion", "db_sys")
os.makedirs(db_dir, exist_ok=True)
database_file = os.path.join(db_dir, "database.json")
backup_file = os.path.join(db_dir, "backup.json")

lista_estudiantes = []
datos_estudiantes = {}

def cargar_datos():
    global datos_estudiantes, lista_estudiantes
    if os.path.exists(database_file):
        with open(database_file, "r") as file:
            datos_estudiantes = json.load(file)
            lista_estudiantes = [(rut_estu, data["nombre"]) for rut_estu, data in datos_estudiantes.items()]
    else:
        datos_estudiantes = {}
    return datos_estudiantes

def guardar_datos():
    with open(database_file, "w") as file:
        json.dump(datos_estudiantes, file, indent=4)

def agregar_estudiante(RUT_estudiante, nombre, matricula):
    if RUT_estudiante in datos_estudiantes:
        print("Error: El estudiante con esta identificación ya existe.")
        return datos_estudiantes
    
    print("Seleccione una carrera de las opciones disponibles:")
    carreras_disponibles = list(CARRERAS.keys())  # Obtener las carreras como lista
    
    for i, carrera in enumerate(carreras_disponibles, start=1):
        print(f"{i}) {carrera}")
    
    while True:
        try:
            carrera_opcion = int(input("Ingrese el número de la carrera: ")) - 1
            if 0 <= carrera_opcion < len(carreras_disponibles):
                carrera_seleccionada = carreras_disponibles[carrera_opcion]
                break
            else:
                print("Por favor, ingrese un número dentro del rango de opciones.")
        except ValueError:
            print("Entrada no válida, por favor ingrese un número.")
    
    cursos = list(CARRERAS[carrera_seleccionada])
    
    # Crear y almacenar la tupla del estudiante
    estudiante_tupla = (RUT_estudiante, nombre)
    lista_estudiantes.append(estudiante_tupla)
    
    datos_estudiantes[RUT_estudiante] = {
        "nombre": nombre,
        "matricula": matricula,
        "carrera": carrera_seleccionada,
        "cursos": cursos,
        "calificaciones": [{"curso": curso, "nota": None} for curso in cursos]
    }
    
    print(f"Estudiante {nombre} agregado con éxito a la carrera {carrera_seleccionada}.")
    return datos_estudiantes

def modificar_datos_estudiante(RUT_estudiante, nombre=None, matricula=None, cursos=None):
    if RUT_estudiante not in datos_estudiantes:
        print("Error: Estudiante no encontrado.")
        return datos_estudiantes
    
    if nombre:
        datos_estudiantes[RUT_estudiante]["nombre"] = nombre
    if matricula:
        datos_estudiantes[RUT_estudiante]["matricula"] = matricula
    if cursos is not None:
        datos_estudiantes[RUT_estudiante]["cursos"] = cursos
    print(f"Estudiante {RUT_estudiante} actualizado con éxito.")
    return datos_estudiantes

def visualizar_estudiantes():
    if not lista_estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    # Preparar lista de diccionarios para crear el DataFrame
    data = [
        {
            "RUT": rut_estu,
            "Nombre": datos_estudiantes[rut_estu]["nombre"],
            "Matrícula": datos_estudiantes[rut_estu]["matricula"]
        }
        for rut_estu, _ in lista_estudiantes
    ]  
    df = pd.DataFrame(data)
    print(df.to_string(index=False))

def eliminar_estudiante(RUT_estudiante):
    visualizar_estudiantes()
    if RUT_estudiante not in datos_estudiantes:
        print("Error: Estudiante no encontrado.")
        return datos_estudiantes
    
    # Recuperamos los datos del estudiante antes de eliminarlo
    estudiante_respaldo = datos_estudiantes.pop(RUT_estudiante)
    global lista_estudiantes
    lista_estudiantes = [estudiante for estudiante in lista_estudiantes if estudiante[0] != RUT_estudiante]
    guardar_datos() # Actualizamos la base de datos
        
    # Guardar el estudiante eliminado en el archivo 'backup.json'
    if os.path.exists(backup_file):
        with open(backup_file, "r") as file:
            backup_data = json.load(file)
    else:
        backup_data = {}
    
    backup_data[RUT_estudiante] = estudiante_respaldo
    with open(backup_file, "w") as file:
        json.dump(backup_data, file, indent=4)
    print(f"Estudiante {RUT_estudiante} eliminado y respaldado correctamente en 'backup.json'.")
    return datos_estudiantes