import json
import os
import pandas as pd
import gestion.gestion_universidad as gtu

db_dir = os.path.join("gestion", "db_sys")
database_file = os.path.join(db_dir, "database.json")

def cargar_datos():
    if os.path.exists(database_file):
        with open(database_file, "r") as file:
            return json.load(file)
    return {}

def guardar_datos(datos_estudiantes):
    with open(database_file, "w") as file:
        json.dump(datos_estudiantes, file, indent=4)

def visualizar_calificaciones_carrera(carrera):
    gtu.visualizar_carreras_y_cursos()  # Mostrar las carreras y sus cursos antes de pedir la entrada
    carrera = input("Ingrese el nombre de la carrera: ")
    datos_estudiantes = cargar_datos()
    data = []
    
    for rut, estudiante in datos_estudiantes.items():
        if estudiante.get("carrera") == carrera:
            calificaciones = {cal["curso"]: cal["nota"] for cal in estudiante["calificaciones"]}
            data.append({
                "RUT": rut,
                "Nombre": estudiante["nombre"],
                **calificaciones
            })
    if data:
        df = pd.DataFrame(data)
        print(f"Calificaciones de estudiantes en la carrera {carrera}:")
        print(df.to_string(index=False))
    else:
        print(f"No se encontraron estudiantes en la carrera {carrera}.")

def visualizar_calificaciones_sede(sede):
    gtu.visualizar_sedes()  # Mostrar sedes disponibles antes de pedir la entrada
    sede = input("Ingrese el nombre de la sede: ")
    
    datos_estudiantes = cargar_datos()
    data = []
    for rut, estudiante in datos_estudiantes.items():
        if estudiante.get("sede") == sede:
            calificaciones = {cal["curso"]: cal["nota"] for cal in estudiante["calificaciones"]}
            data.append({
                "RUT": rut,
                "Nombre": estudiante["nombre"],
                **calificaciones
            })
    
    if data:
        df = pd.DataFrame(data)
        print(f"Calificaciones de estudiantes en la sede {sede}:")
        print(df.to_string(index=False))
    else:
        print(f"No se encontraron estudiantes en la sede {sede}.")

def modificar_calificacion():
    # Mostrar opciones de carrera y solicitar una selección
    gtu.visualizar_carreras_y_cursos()  # Mostrar las carreras disponibles
    carrera = input("Ingrese el nombre de la carrera: ")
    
    # Cargar datos y filtrar estudiantes por la carrera seleccionada
    datos_estudiantes = cargar_datos()
    estudiantes_carrera = {rut: est for rut, est in datos_estudiantes.items() if est.get("carrera") == carrera}
    
    if estudiantes_carrera:
        data = [{"RUT": rut, "Nombre": est["nombre"]} for rut, est in estudiantes_carrera.items()]
        df = pd.DataFrame(data)
        print(f"\nEstudiantes en la carrera '{carrera}':")
        print(df.to_string(index=False))
    else:
        print(f"No se encontraron estudiantes en la carrera '{carrera}'.")
        return

    rut_estudiante = input("Ingrese el RUT del estudiante: ")
    estudiante = estudiantes_carrera.get(rut_estudiante)
    if not estudiante:
        print("Error: Estudiante no encontrado en la carrera especificada.")
        return

    print("\nCursos del estudiante:")
    for cal in estudiante["calificaciones"]:
        print(f"- {cal['curso']}: {cal['nota']}")
    
    curso = input("Ingrese el nombre del curso a modificar: ")
    nueva_calificacion = float(input("Ingrese la nueva calificación: "))
    
    # Actualizar o asignar calificación
    for cal in estudiante["calificaciones"]:
        if cal["curso"] == curso:
            cal["nota"] = nueva_calificacion
            guardar_datos(datos_estudiantes)
            print(f"Calificación actualizada para el curso '{curso}' del estudiante con RUT {rut_estudiante}.")
            return
    
    print(f"Error: El curso '{curso}' no está asignado al estudiante.")