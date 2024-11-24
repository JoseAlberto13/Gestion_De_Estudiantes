import tkinter as tk
from tkinter import messagebox, simpledialog
import json


# --- Funciones auxiliares ---
def verificador_rut(rut):
    """
    Verifica la validez del RUT ingresado.
    """
    if "-" in rut:
        rut = rut.replace("-", "")
    else:
        return False

    if len(rut) not in range(8, 10):
        return False

    verificador = rut[-1]
    rut = rut[:-1]
    suma = 0

    if verificador == "0":
        verificador = 11
    elif verificador.lower() == "k":
        verificador = 10
    else:
        try:
            verificador = int(verificador)
        except ValueError:
            return False

    try:
        for i, factor in enumerate([3, 2, 7, 6, 5, 4, 3, 2]):
            suma += int(rut[i]) * factor
    except (ValueError, IndexError):
        return False

    restante = suma % 11
    validador = 11 - restante
    return verificador == validador


# --- Funciones principales ---
def agregar_info_estudiante(lista_estudiantes, calificaciones, cursos):
    """
    Agrega información de un estudiante mediante formularios.
    """
    def guardar():
        nombre = entry_nombre.get()
        rut = entry_rut.get()
        matricula = entry_matricula.get()

        if not nombre or not rut or not matricula:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        if not verificador_rut(rut):
            messagebox.showerror("Error", "El RUT ingresado no es válido.")
            return

        estudiante = (nombre, rut, matricula)
        lista_estudiantes.append(estudiante)
        calificaciones.append([rut, {}])
        cursos.append([rut, []])
        messagebox.showinfo("Éxito", f"Estudiante {nombre} agregado exitosamente.")
        ventana.destroy()

    ventana = tk.Tk()
    ventana.title("Agregar Estudiante")
    ventana.geometry("300x200")

    tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=0, column=1)

    tk.Label(ventana, text="RUT:").grid(row=1, column=0, padx=10, pady=10)
    entry_rut = tk.Entry(ventana)
    entry_rut.grid(row=1, column=1)

    tk.Label(ventana, text="Matrícula:").grid(row=2, column=0, padx=10, pady=10)
    entry_matricula = tk.Entry(ventana)
    entry_matricula.grid(row=2, column=1)

    tk.Button(ventana, text="Guardar", command=guardar).grid(row=3, column=0, columnspan=2, pady=20)
    ventana.mainloop()


def modificar_info_estudiante(lista_estudiantes):
    """
    Modifica información de un estudiante mediante un formulario.
    """
    def buscar():
        rut = entry_rut.get()
        estudiante = next((e for e in lista_estudiantes if e[1] == rut), None)

        if estudiante:
            entry_nombre.insert(0, estudiante[0])
            entry_matricula.insert(0, estudiante[2])
            btn_guardar.config(state="normal")
        else:
            messagebox.showerror("Error", "Estudiante no encontrado.")

    def guardar():
        nombre = entry_nombre.get()
        matricula = entry_matricula.get()
        rut = entry_rut.get()

        for i, estudiante in enumerate(lista_estudiantes):
            if estudiante[1] == rut:
                lista_estudiantes[i] = (nombre, rut, matricula)
                messagebox.showinfo("Éxito", "Información del estudiante actualizada.")
                ventana.destroy()
                return

    ventana = tk.Tk()
    ventana.title("Modificar Estudiante")
    ventana.geometry("300x300")

    tk.Label(ventana, text="RUT:").grid(row=0, column=0, padx=10, pady=10)
    entry_rut = tk.Entry(ventana)
    entry_rut.grid(row=0, column=1)

    tk.Button(ventana, text="Buscar", command=buscar).grid(row=1, column=0, columnspan=2, pady=10)

    tk.Label(ventana, text="Nombre:").grid(row=2, column=0, padx=10, pady=10)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=2, column=1)

    tk.Label(ventana, text="Matrícula:").grid(row=3, column=0, padx=10, pady=10)
    entry_matricula = tk.Entry(ventana)
    entry_matricula.grid(row=3, column=1)

    btn_guardar = tk.Button(ventana, text="Guardar", state="disabled", command=guardar)
    btn_guardar.grid(row=4, column=0, columnspan=2, pady=20)

    ventana.mainloop()


def eliminar_info_estudiante(lista_estudiantes, db_backup):
    """
    Elimina un estudiante tras confirmar la acción.
    """
    def eliminar():
        rut = entry_rut.get()
        for i, estudiante in enumerate(lista_estudiantes):
            if estudiante[1] == rut:
                db_backup["estudiantes"]["info_estudiantes"].append(estudiante)
                lista_estudiantes.pop(i)
                messagebox.showinfo("Éxito", "Estudiante eliminado correctamente.")
                ventana.destroy()
                return
        messagebox.showerror("Error", "Estudiante no encontrado.")

    ventana = tk.Tk()
    ventana.title("Eliminar Estudiante")
    ventana.geometry("300x150")

    tk.Label(ventana, text="RUT:").grid(row=0, column=0, padx=10, pady=10)
    entry_rut = tk.Entry(ventana)
    entry_rut.grid(row=0, column=1)

    tk.Button(ventana, text="Eliminar", command=eliminar).grid(row=1, column=0, columnspan=2, pady=20)
    ventana.mainloop()


def visualizar_estudiantes(lista_estudiantes):
    """
    Muestra todos los estudiantes en una nueva ventana.
    """
    ventana = tk.Tk()
    ventana.title("Estudiantes")
    ventana.geometry("400x300")

    tk.Label(ventana, text="Estudiantes Registrados", font=("Arial", 16)).pack(pady=10)

    text_box = tk.Text(ventana, wrap="none", width=50, height=15)
    text_box.pack(pady=10)

    if lista_estudiantes:
        for estudiante in lista_estudiantes:
            text_box.insert("end", f"Nombre: {estudiante[0]}, RUT: {estudiante[1]}, Matrícula: {estudiante[2]}\n")
    else:
        text_box.insert("end", "No hay estudiantes registrados.\n")

    tk.Button(ventana, text="Cerrar", command=ventana.destroy).pack(pady=10)
    ventana.mainloop()