import tkinter as tk
from tkinter import messagebox

def agregar_sede(sedes, entry_sede):
    nueva_sede = entry_sede.get()
    if nueva_sede:
        sedes = list(sedes)
        sedes.append(nueva_sede)
        sedes = tuple(sedes)
        messagebox.showinfo("Éxito", "Sede agregada con éxito")
        entry_sede.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Debe ingresar un nombre para la sede.")
    return sedes

def modificar_sede(sedes, entry_sede, entry_nueva_sede):
    sede = entry_sede.get()
    if sede in sedes:
        nueva_sede = entry_nueva_sede.get()
        if nueva_sede:
            sedes = list(sedes)
            indice = sedes.index(sede)
            sedes[indice] = nueva_sede
            sedes = tuple(sedes)
            messagebox.showinfo("Éxito", "Sede modificada con éxito")
            entry_sede.delete(0, tk.END)
            entry_nueva_sede.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Debe ingresar el nuevo nombre de la sede.")
    else:
        messagebox.showerror("Error", "Sede no encontrada.")
    return sedes

def eliminar_sede(sedes, db_backup, entry_sede):
    sede = entry_sede.get()
    if sede in sedes:
        sedes = list(sedes)
        db_backup['sedes'].append(sede)
        sedes.remove(sede)
        sedes = tuple(sedes)
        messagebox.showinfo("Éxito", "Sede eliminada con éxito")
        entry_sede.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Sede no encontrada.")
    return sedes

def visualizar_sedes(sedes, text_widget):
    text_widget.delete(1.0, tk.END)
    if sedes:
        for sede in sedes:
            text_widget.insert(tk.END, f"{sede}\n")
    else:
        text_widget.insert(tk.END, "No hay sedes registradas.")
