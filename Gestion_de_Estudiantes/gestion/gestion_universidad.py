import json
import os
import pandas as pd

# Definir la ruta para almacenar las sedes, carreras y cursos
db_dir = os.path.join("gestion", "db_sys")
os.makedirs(db_dir, exist_ok=True)
carreras_file = os.path.join(db_dir, "carreras.json")
sedes_file = os.path.join(db_dir, "sedes.json")

def cargar_carreras():
    if os.path.exists(carreras_file):
        with open(carreras_file, "r") as file:
            return json.load(file)
    return {}

def cargar_sedes():
    if os.path.exists(sedes_file):
        with open(sedes_file, "r") as file:
            return json.load(file)
    return {}

# Guardar sedes en el archivo JSON
def guardar_sedes(sedes):
    with open(sedes_file, "w") as file:
        json.dump(sedes, file, indent=4)
    print("Datos de sedes guardados correctamente en 'sedes.json'.")

# Crear una nueva sede
def crear_sede(nombre_sede, direccion):
    sedes = cargar_sedes()
    if nombre_sede in sedes:
        print("Error: La sede ya existe.")
        return
    
    sedes[nombre_sede] = {"nombre": nombre_sede, "direccion": direccion}
    guardar_sedes(sedes)
    print(f"Sede '{nombre_sede}' creada con éxito.")

# Actualizar información de una sede
def actualizar_sede(nombre_sede, nueva_direccion):
    sedes = cargar_sedes()
    if nombre_sede not in sedes:
        print("Error: La sede no existe.")
        return
    
    sedes[nombre_sede]["direccion"] = nueva_direccion
    guardar_sedes(sedes)
    print(f"Sede '{nombre_sede}' actualizada con éxito.")

# Eliminar una sede
def eliminar_sede(nombre_sede):
    sedes = cargar_sedes()
    if nombre_sede in sedes:
        del sedes[nombre_sede]
        guardar_sedes(sedes)
        print(f"Sede '{nombre_sede}' eliminada con éxito.")
    else:
        print("Error: La sede no existe.")

# Visualizar todas las carreras y cursos usando pandas
def visualizar_carreras_y_cursos():
    carreras = cargar_carreras()
    if not carreras:
        print("No hay carreras registradas.")
        return
    
    # Crear una lista de diccionarios para preparar los datos en formato de tabla
    data = []
    for carrera, cursos in carreras.items():
        if cursos:
            for curso in cursos:
                data.append({"Carrera": carrera, "Curso": curso})
        else:
            data.append({"Carrera": carrera, "Curso": "Sin cursos registrados"})
    
    # Crear DataFrame de pandas
    df = pd.DataFrame(data)
    print("\nCarreras y sus cursos:")
    print(df.to_string(index=False))

# Visualizar todas las sedes usando pandas
def visualizar_sedes():
    sedes = cargar_sedes()
    data = [{"ID": sid, "Nombre": info["nombre"], "Dirección": info["direccion"]} for sid, info in sedes.items()]
    df = pd.DataFrame(data)
    print("\nSedes disponibles:")
    print(df.to_string(index=False))