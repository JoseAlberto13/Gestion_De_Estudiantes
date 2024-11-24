import json
import tkinter as tk
from tkinter import messagebox

def cargar_datos_json_cursos():
    try:
        with open("gestion/main_db.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            return tuple(datos.get("cursos", []))
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def agregar_curso(cursos, entry_curso):
    nuevo_curso = entry_curso.get()
    if nuevo_curso:
        cursos = list(cursos)
        cursos.append(nuevo_curso)
        cursos = tuple(cursos)
        messagebox.showinfo("Éxito", f"Curso '{nuevo_curso}' agregado con éxito.")
        entry_curso.delete(0, tk.END)
        return cursos
    else:
        messagebox.showerror("Error", "Debe ingresar el nombre de un curso.")
        return cursos

def actualizar_info_cursos(cursos, db_json):
    db_json.update({"cursos": cursos})
    return db_json

def crear_interfaz(cursos, db_json):
    # Crear ventana principal
    root = tk.Tk()
    root.title("Gestión de Cursos")

    # Crear entrada y etiqueta para el curso
    label_curso = tk.Label(root, text="Nombre del curso a agregar:")
    label_curso.pack(pady=10)

    entry_curso = tk.Entry(root)
    entry_curso.pack(pady=10)

    # Función para agregar curso
    def on_agregar_curso():
        nonlocal cursos
        cursos = agregar_curso(cursos, entry_curso)

    # Función para guardar cambios en el archivo
    def on_guardar_cambios():
        db_json = actualizar_info_cursos(cursos, db_json)
        with open("gestion/main_db.json", "w", encoding="utf-8") as archivo:
            json.dump(db_json, archivo, ensure_ascii=False, indent=4)
        messagebox.showinfo("Guardado", "Los cambios han sido guardados correctamente.")

    # Botón para agregar curso
    btn_agregar = tk.Button(root, text="Agregar Curso", command=on_agregar_curso)
    btn_agregar.pack(pady=10)

    # Botón para guardar cambios
    btn_guardar = tk.Button(root, text="Guardar Cambios", command=on_guardar_cambios)
    btn_guardar.pack(pady=10)

    # Botón para salir
    btn_salir = tk.Button(root, text="Salir", command=root.quit)
    btn_salir.pack(pady=10)

    # Iniciar la interfaz gráfica
    root.mainloop()