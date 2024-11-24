import json
from tkinter import Tk, Button, Label, Listbox, Scrollbar, messagebox


# --- Funciones de manejo de JSON ---
def cargar_datos_json_sedes():
    """
    Carga las sedes desde el archivo main_db.json.
    """
    try:
        with open("gestion/main_db.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            return tuple(datos.get("sedes", []))
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showerror("Error", "No se pudo cargar el archivo de datos.")
        return ()


def mostrar_sedes():
    """
    Muestra las sedes disponibles en una ventana nueva.
    """
    sedes = cargar_datos_json_sedes()
    if not sedes:
        messagebox.showinfo("Sedes", "No hay sedes registradas.")
        return

    # Crear una ventana para mostrar las sedes
    ventana_sedes = Tk()
    ventana_sedes.title("Sedes Disponibles")
    ventana_sedes.geometry("300x300")

    Label(ventana_sedes, text="Lista de Sedes", font=("Arial", 14)).pack(pady=10)

    # Listbox para mostrar las sedes
    frame_lista = Scrollbar(ventana_sedes)
    frame_lista.pack(side="right", fill="y")
    
    lista_sedes = Listbox(ventana_sedes, yscrollcommand=frame_lista.set, width=40, height=15)
    for i, sede in enumerate(sedes, start=1):
        lista_sedes.insert(i, f"{i}. {sede}")

    lista_sedes.pack(pady=10)
    frame_lista.config(command=lista_sedes.yview)

    Button(ventana_sedes, text="Cerrar", command=ventana_sedes.destroy).pack(pady=10)
    ventana_sedes.mainloop()


# --- Interfaz gráfica principal ---
def main_menu():
    """
    Menú principal para gestionar las opciones.
    """
    root = Tk()
    root.title("Sistema de Gestión - Menú Principal")
    root.geometry("300x200")

    Label(root, text="Gestión de Sedes", font=("Arial", 16)).pack(pady=10)

    Button(root, text="Mostrar Sedes", command=mostrar_sedes).pack(pady=10)
    Button(root, text="Salir", command=root.quit).pack(pady=10)

    root.mainloop()


# Ejecutar la interfaz gráfica
if __name__ == "__main__":
    main_menu()

