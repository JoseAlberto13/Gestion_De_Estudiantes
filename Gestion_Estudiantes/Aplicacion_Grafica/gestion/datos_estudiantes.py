import json
import os
from tkinter import Tk, Button, Label, messagebox, filedialog

# --- Funciones de manejo de JSON ---
def cargar_datos_json():
    if not os.path.exists("gestion/main_db.json"):
        datos_default = {
            "estudiantes": {
                "info_estudiantes": [],
                "cursos": [],
                "calificaciones": []
            },
            "cursos": [],
            "sedes": []
        }
        with open("gestion/main_db.json", 'w') as archivo:
            json.dump(datos_default, archivo, indent=2, separators=(',', ': '))
        return datos_default
    else:
        try:
            with open("gestion/main_db.json", "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                return datos
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showerror("Error", "No se pudo cargar el archivo de datos.")
            return {}

def guardar_datos(db_json):
    try:
        with open("gestion/main_db.json", 'w') as archivo:
            json.dump(db_json, archivo, indent=2, separators=(',', ': '))
        messagebox.showinfo("Éxito", "Datos guardados correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar el archivo de datos: {e}")

def mostrar_info_estudiantes():
    db_json = cargar_datos_json()
    estudiantes = db_json.get("estudiantes", {}).get("info_estudiantes", [])
    if estudiantes:
        estudiantes_str = "\n".join([f"{i + 1}. {est}" for i, est in enumerate(estudiantes)])
        messagebox.showinfo("Estudiantes", estudiantes_str)
    else:
        messagebox.showinfo("Estudiantes", "No hay estudiantes registrados.")

# --- Función para cargar los datos de backup ---
def cargar_backup():
    if not os.path.exists("gestion/db_sys.json"):
        # Si no existe el archivo de backup, crea uno con datos predeterminados
        datos_default = {
            "estudiantes": {
                "info_estudiantes": [],
                "cursos": [],
                "calificaciones": []
            },
            "cursos": [],
            "sedes": []
        }
        with open("gestion/db_sys.json", 'w') as archivo:
            json.dump(datos_default, archivo, indent=2, separators=(',', ': '))
        return datos_default
    else:
        try:
            with open("gestion/db_sys.json", "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                return datos
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showerror("Error", "No se pudo cargar el archivo de backup.")
            return {}

def guardar_backup(db_backup):
    try:
        with open("gestion/db_sys.json", 'w') as archivo:
            json.dump(db_backup, archivo, indent=2, separators=(',', ': '))
        messagebox.showinfo("Éxito", "Backup guardado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar el archivo de backup: {e}")

# --- Interfaz gráfica ---
def main_menu():
    root = Tk()
    root.title("Sistema de Gestión - Datos")
    root.geometry("400x300")

    # Etiqueta principal
    Label(root, text="Gestión de Datos", font=("Arial", 16)).pack(pady=10)

    # Botones para acciones principales
    Button(root, text="Cargar Datos", command=cargar_datos_json).pack(pady=5)
    Button(root, text="Guardar Datos", command=lambda: guardar_datos(cargar_datos_json())).pack(pady=5)
    Button(root, text="Mostrar Información de Estudiantes", command=mostrar_info_estudiantes).pack(pady=5)
    Button(root, text="Cargar Backup", command=cargar_backup).pack(pady=5)  # Botón para cargar backup
    Button(root, text="Guardar Backup", command=lambda: guardar_backup(cargar_backup())).pack(pady=5)  # Botón para guardar backup
    Button(root, text="Salir", command=root.quit).pack(pady=20)

    root.mainloop()

# Ejecutar la interfaz gráfica
if __name__ == "__main__":
    main_menu()