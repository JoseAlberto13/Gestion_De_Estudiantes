import tkinter as tk
from tkinter import messagebox
import gestion as gt  # Importa todos los módulos definidos anteriormente
import os

# Variables globales
db_json = gt.cargar_datos_json()
db_backup = gt.cargar_backup()

# Función para iniciar la ventana principal
def iniciar_ventana_principal():
    ventana = tk.Tk()
    ventana.title("Sistema de Gestión Universitaria")
    ventana.geometry("600x400")  # Tamaño de la ventana

    # Título
    titulo = tk.Label(ventana, text="Bienvenido al Sistema de Gestión Universitaria", font=("Arial", 16))
    titulo.pack(pady=20)

    # Botones para los menús
    boton_estudiantes = tk.Button(ventana, text="Menú de Estudiantes", width=30, height=2, command=menu_estudiantes)
    boton_estudiantes.pack(pady=10)

    boton_cursos = tk.Button(ventana, text="Menú de Cursos", width=30, height=2, command=menu_cursos)
    boton_cursos.pack(pady=10)

    boton_universidad = tk.Button(ventana, text="Menú de Universidad", width=30, height=2, command=menu_universidad)
    boton_universidad.pack(pady=10)

    boton_salir = tk.Button(ventana, text="Salir", width=30, height=2, command=ventana.quit)
    boton_salir.pack(pady=10)

    ventana.mainloop()

# Función para manejar el menú de estudiantes
def menu_estudiantes():
    # Crear una nueva ventana para el menú de estudiantes
    ventana_estudiantes = tk.Toplevel()
    ventana_estudiantes.title("Menú de Estudiantes")
    
    # Opciones de estudiantes
    tk.Button(ventana_estudiantes, text="Agregar información de un estudiante", command=agregar_estudiante).pack(pady=10)
    tk.Button(ventana_estudiantes, text="Modificar información de un estudiante", command=modificar_estudiante).pack(pady=10)
    tk.Button(ventana_estudiantes, text="Eliminar información de un estudiante", command=eliminar_estudiante).pack(pady=10)
    tk.Button(ventana_estudiantes, text="Visualizar todos los estudiantes", command=visualizar_estudiantes).pack(pady=10)
    tk.Button(ventana_estudiantes, text="Volver", command=ventana_estudiantes.destroy).pack(pady=10)

# Funciones de estudiantes
def agregar_estudiante():
    info_estudiantes = db_json["estudiantes"]["info_estudiantes"]
    calificaciones = db_json["estudiantes"]["calificaciones"]
    cursos = db_json["estudiantes"]["cursos"]
    info_estudiantes, calificaciones, cursos = gt.agregar_info_estudiante(info_estudiantes, calificaciones, cursos)
    messagebox.showinfo("Éxito", "Información de estudiante agregada con éxito")

def modificar_estudiante():
    info_estudiantes = db_json["estudiantes"]["info_estudiantes"]
    gt.visualizar_estudiantes(info_estudiantes)
    info_estudiantes = gt.modificar_info_estudiante(info_estudiantes)
    messagebox.showinfo("Éxito", "Información de estudiante modificada con éxito")

def eliminar_estudiante():
    info_estudiantes = db_json["estudiantes"]["info_estudiantes"]
    info_estudiantes = gt.eliminar_info_estudiante(info_estudiantes, db_backup)
    messagebox.showinfo("Éxito", "Información de estudiante eliminada con éxito")

def visualizar_estudiantes():
    info_estudiantes = db_json["estudiantes"]["info_estudiantes"]
    gt.visualizar_estudiantes(info_estudiantes)

# Función para manejar el menú de cursos
def menu_cursos():
    ventana_cursos = tk.Toplevel()
    ventana_cursos.title("Menú de Cursos")

    tk.Button(ventana_cursos, text="Agregar curso", command=agregar_curso).pack(pady=10)
    tk.Button(ventana_cursos, text="Modificar curso", command=modificar_curso).pack(pady=10)
    tk.Button(ventana_cursos, text="Eliminar curso", command=eliminar_curso).pack(pady=10)
    tk.Button(ventana_cursos, text="Visualizar cursos", command=visualizar_cursos).pack(pady=10)
    tk.Button(ventana_cursos, text="Volver", command=ventana_cursos.destroy).pack(pady=10)

# Funciones de cursos
def agregar_curso():
    cursos = db_json["cursos"]
    cursos = gt.agregar_curso(cursos)
    messagebox.showinfo("Éxito", "Curso agregado con éxito")

def modificar_curso():
    cursos = db_json["cursos"]
    gt.visualizar_cursos(cursos)
    cursos = gt.modificar_curso(cursos)
    messagebox.showinfo("Éxito", "Curso modificado con éxito")

def eliminar_curso():
    cursos = db_json["cursos"]
    cursos = gt.eliminar_curso(cursos, db_backup)
    messagebox.showinfo("Éxito", "Curso eliminado con éxito")

def visualizar_cursos():
    cursos = db_json["cursos"]
    gt.visualizar_cursos(cursos)

# Función para manejar el menú de universidad
def menu_universidad():
    ventana_universidad = tk.Toplevel()
    ventana_universidad.title("Menú de Universidad")

    tk.Button(ventana_universidad, text="Agregar sede de la universidad", command=agregar_sede).pack(pady=10)
    tk.Button(ventana_universidad, text="Modificar sede de la universidad", command=modificar_sede).pack(pady=10)
    tk.Button(ventana_universidad, text="Eliminar sede de la universidad", command=eliminar_sede).pack(pady=10)
    tk.Button(ventana_universidad, text="Visualizar sedes de la universidad", command=visualizar_sedes).pack(pady=10)
    tk.Button(ventana_universidad, text="Volver", command=ventana_universidad.destroy).pack(pady=10)

# Funciones de universidad
def agregar_sede():
    sedes = db_json["sedes"]
    sedes = gt.agregar_sede(sedes)
    messagebox.showinfo("Éxito", "Sede agregada con éxito")

def modificar_sede():
    sedes = db_json["sedes"]
    gt.visualizar_sedes(sedes)
    sedes = gt.modificar_sede(sedes)
    messagebox.showinfo("Éxito", "Sede modificada con éxito")

def eliminar_sede():
    sedes = db_json["sedes"]
    sedes = gt.eliminar_sede(sedes, db_backup)
    messagebox.showinfo("Éxito", "Sede eliminada con éxito")

def visualizar_sedes():
    sedes = db_json["sedes"]
    gt.visualizar_sedes(sedes)

# Ejecutar la aplicación
if __name__ == "__main__":
    iniciar_ventana_principal()
