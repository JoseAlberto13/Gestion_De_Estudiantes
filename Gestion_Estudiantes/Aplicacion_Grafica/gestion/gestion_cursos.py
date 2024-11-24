import tkinter as tk
from tkinter import messagebox

def modificar_curso(cursos, entry_curso, entry_nuevo_curso):
    curso = entry_curso.get()
    if curso in cursos:
        nuevo_curso = entry_nuevo_curso.get()
        if nuevo_curso:
            cursos = list(cursos)
            indice = cursos.index(curso)
            cursos[indice] = nuevo_curso
            cursos = tuple(cursos)
            messagebox.showinfo("Éxito", "Curso modificado con éxito")
            entry_curso.delete(0, tk.END)
            entry_nuevo_curso.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Debe ingresar el nuevo nombre del curso.")
    else:
        messagebox.showerror("Error", "Curso no encontrado.")
    return cursos

def eliminar_curso(cursos, db_backup, entry_curso):
    curso = entry_curso.get()
    if curso in cursos:
        cursos = list(cursos)
        db_backup["cursos"].append(curso)
        cursos.remove(curso)
        cursos = tuple(cursos)
        messagebox.showinfo("Éxito", "Curso eliminado con éxito")
        entry_curso.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Curso no encontrado.")
    return cursos

def visualizar_cursos(cursos, text_widget):
    text_widget.delete(1.0, tk.END)
    if cursos:
        for curso in cursos:
            text_widget.insert(tk.END, f"{curso}\n")
    else:
        text_widget.insert(tk.END, "No hay cursos registrados.")

def agregar_curso_estudiante(cursos, cursos_estudiante, entry_rut, entry_curso):
    rut = entry_rut.get()
    for estudiante in cursos_estudiante:
        if estudiante[0] == rut:
            nuevo_curso = entry_curso.get()
            if nuevo_curso in cursos:
                estudiante[1].append(nuevo_curso)
                messagebox.showinfo("Éxito", "Curso agregado al estudiante con éxito")
                entry_rut.delete(0, tk.END)
                entry_curso.delete(0, tk.END)
                return cursos_estudiante
            else:
                messagebox.showerror("Error", "El curso no es válido o no se encuentra en la lista.")
                return cursos_estudiante
    else:
        messagebox.showerror("Error", "Estudiante no encontrado.")
        return cursos_estudiante

def eliminar_curso_estudiante(cursos_estudiante, db_backup, entry_rut, entry_curso):
    rut = entry_rut.get()
    for estudiante in cursos_estudiante:
        if estudiante[0] == rut:
            curso = entry_curso.get()
            if curso in estudiante[1]:
                db_backup['estudiantes']['cursos'].append(curso)
                estudiante[1].remove(curso)
                messagebox.showinfo("Éxito", "Curso eliminado al estudiante con éxito")
                entry_rut.delete(0, tk.END)
                entry_curso.delete(0, tk.END)
                return cursos_estudiante
            else:
                messagebox.showerror("Error", "El curso no es válido o no se encuentra en la lista.")
                return cursos_estudiante
    else:
        messagebox.showerror("Error", "Estudiante no encontrado.")
        return cursos_estudiante

def visualizar_cursos_estudiantes(cursos_estudiantes, text_widget):
    text_widget.delete(1.0, tk.END)
    for estudiante in cursos_estudiantes:
        rut = estudiante[0]
        cursos = estudiante[1]
        text_widget.insert(tk.END, f"Cursos del estudiante con RUT {rut}:\n")
        if cursos:
            for curso in cursos:
                text_widget.insert(tk.END, f"  - {curso}\n")
        else:
            text_widget.insert(tk.END, "  No hay cursos\n")