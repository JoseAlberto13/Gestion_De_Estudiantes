import tkinter as tk
from tkinter import messagebox
from .datos_estudiantes import cargar_datos_json

def datos_calificaciones():
    db_json = cargar_datos_json()
    calificaciones = db_json["calificaciones"]
    return calificaciones

def actualizar_info_calificaciones(calificaciones, db_json):
    db_json.update({"calificaciones": calificaciones})
    return db_json

def agregar_calificaciones(calificaciones, entry_rut, entry_materia, entry_calificacion):
    rut = entry_rut.get()
    for estudiante in calificaciones:
        if rut == estudiante[0]:
            materia = entry_materia.get()
            if materia in estudiante[1]:
                calificacion = entry_calificacion.get()
                if calificacion:
                    estudiante[1][materia].append(calificacion)
                    messagebox.showinfo("Éxito", f"Calificación de {calificacion} agregada a {materia} para el estudiante con RUT {rut}")
                    entry_rut.delete(0, tk.END)
                    entry_materia.delete(0, tk.END)
                    entry_calificacion.delete(0, tk.END)
                    return calificaciones
                else:
                    messagebox.showerror("Error", "Debe ingresar una calificación.")
                    return calificaciones
            else:
                messagebox.showerror("Error", "Materia no válida.")
                return calificaciones
    else:
        messagebox.showerror("Error", "RUT no encontrado.")
        return calificaciones

def eliminar_calificaciones(calificaciones, db_backup, entry_rut, entry_materia, entry_indice):
    rut = entry_rut.get()
    for estudiante in calificaciones:
        if rut == estudiante[0]:
            materia = entry_materia.get()
            if materia in estudiante[1]:
                try:
                    indice = int(entry_indice.get())
                    if 1 <= indice <= len(estudiante[1][materia]):
                        db_backup['estudiantes']['calificaciones'].append(estudiante[1][materia][indice - 1])
                        estudiante[1][materia].pop(indice - 1)
                        messagebox.showinfo("Éxito", f"Calificación borrada de {materia} para el estudiante con RUT {rut}")
                        entry_rut.delete(0, tk.END)
                        entry_materia.delete(0, tk.END)
                        entry_indice.delete(0, tk.END)
                        return calificaciones
                    else:
                        messagebox.showerror("Error", "Índice fuera de rango. Intente de nuevo.")
                        return calificaciones
                except ValueError:
                    messagebox.showerror("Error", "Entrada no válida. Debe ingresar un número entero.")
                    return calificaciones
            else:
                messagebox.showerror("Error", "Materia no válida.")
                return calificaciones
    else:
        messagebox.showerror("Error", "RUT no encontrado.")
        return calificaciones

def visualizar_calificaciones(calificaciones, text_widget):
    text_widget.delete(1.0, tk.END)
    for estudiante in calificaciones:
        rut = estudiante[0]
        notas = estudiante[1]
        text_widget.insert(tk.END, f"Calificaciones para el estudiante con RUT {rut}:\n")
        for curso, notas_curso in notas.items():
            text_widget.insert(tk.END, f"  {curso}: {notas_curso if notas_curso else 'No hay calificaciones'}\n")