import json
import os

# JSON exclusivamente para la gestion de las carreras y cursos
db_dir = os.path.join("gestion", "db_sys")
os.makedirs(db_dir, exist_ok=True)
carreras_file = os.path.join(db_dir, "carreras.json")

def cargar_carreras():
    if os.path.exists(carreras_file):
        with open(carreras_file, "r") as file:
            return json.load(file)
    return {}

def guardar_carreras(carreras):
    with open(carreras_file, "w") as file:
        json.dump(carreras, file, indent=4)
    print("Datos guardados correctamente en 'carreras.json'.")

def agregar_curso(nombre_carrera, curso):
    carreras = cargar_carreras()
    
    if nombre_carrera not in carreras:
        print("Error: La carrera no existe.")
        return

    if curso in carreras[nombre_carrera]:
        print(f"El curso '{curso}' ya existe en la carrera '{nombre_carrera}'.")
    else:
        carreras[nombre_carrera].append(curso)
        guardar_carreras(carreras)
        print(f"Curso '{curso}' agregado a la carrera '{nombre_carrera}'.")

def actualizar_curso(nombre_carrera, curso_actual, curso_nuevo):
    carreras = cargar_carreras()
    
    if nombre_carrera not in carreras:
        print("Error: La carrera no existe.")
        return
    
    if curso_actual in carreras[nombre_carrera]:
        index = carreras[nombre_carrera].index(curso_actual)
        carreras[nombre_carrera][index] = curso_nuevo
        guardar_carreras(carreras)
        print(f"Curso '{curso_actual}' actualizado a '{curso_nuevo}' en la carrera '{nombre_carrera}'.")
    else:
        print(f"El curso '{curso_actual}' no está registrado en la carrera '{nombre_carrera}'.")

def eliminar_curso(nombre_carrera, curso):
    carreras = cargar_carreras()
    
    if nombre_carrera not in carreras:
        print("Error: La carrera no existe.")
        return
    
    if curso in carreras[nombre_carrera]:
        carreras[nombre_carrera].remove(curso)
        guardar_carreras(carreras)
        print(f"Curso '{curso}' eliminado de la carrera '{nombre_carrera}'.")
    else:
        print(f"El curso '{curso}' no está registrado en la carrera '{nombre_carrera}'.")
