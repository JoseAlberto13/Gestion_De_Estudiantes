import os
import gestion.gestion_estudiantes as gte
import gestion.Calificaciones as gcal
import gestion.gestion_universidad as gtu
import gestion.gestion_cursos as gtc
import gestion.add_new_course as anc

def menu_estudiantes():
    gte.cargar_datos()
    while True:
        os.system("cls")
        print("GESTIÓN DE ESTUDIANTES")
        option = input(
"""
1) Añadir Datos Personales Estudiante
2) Actualizar Datos Personales del Estudiante
3) Visualizar Lista de Estudiantes
4) Eliminar Datos del Estudiante
5) Guardar y Salir
""")
        match option:
            case "1":
                RUT_estudiante = input("Ingrese el RUT del estudiante: ")
                nombre = input("Ingrese el nombre completo: ")
                matricula = input("Ingrese el número de matrícula: ")
                gte.agregar_estudiante(RUT_estudiante, nombre, matricula)
            case "2":
                RUT_estudiante = input("Ingrese el RUT del estudiante a actualizar: ")
                nombre = input("Ingrese el nuevo nombre (o deje vacío para no modificar): ")
                matricula = input("Ingrese la nueva matrícula (o deje vacío para no modificar): ")
                cursos = input("Ingrese los nuevos cursos separados por comas (o deje vacío para no modificar): ")
                cursos = cursos.split(",") if cursos else None
                gte.modificar_datos_estudiante(RUT_estudiante, nombre or None, matricula or None, cursos)
                input("\nPresione una 'Enter' para continuar ")
            case "3":
                gte.visualizar_estudiantes()
                input("\nPresione una 'Enter' para continuar ")
            case "4":
                RUT_estudiante = input("Ingrese el RUT del estudiante a eliminar: ")
                gte.eliminar_estudiante(RUT_estudiante)
                input("\nPresione una 'Enter' para continuar ")
            case "5":
                gte.guardar_datos()
                break

def menu_calificaciones():
    while True:
        os.system("cls")
        print("""
GESTIÓN DE CALIFICACIONES
1) Visualizar calificaciones por carrera
2) Visualizar calificaciones por sede
3) Modificar calificación de un estudiante
4) Volver al menú principal
""")
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                gcal.visualizar_calificaciones_carrera()
            case "2":
                gcal.visualizar_calificaciones_sede()
            case "3":
                gcal.modificar_calificacion()   
            case "4":
                break      
            case _:
                print("Opción no válida.")
        input("\nPresione una 'Enter' para continuar ")
       
def menu_universidad():
    while True:
        os.system("cls")
        print("""
GESTIÓN DE UNIVERSIDAD
1) Crear nueva sede
2) Actualizar sede
3) Eliminar sede
4) Visualizar sedes
5) Visualizar carreras y cursos
6) Volver al menú principal
""")
        opcion = input("Seleccione una opción: ")
        
        match opcion:
            case "1":
                nombre_sede = input("Ingrese el nombre de la nueva sede: ")
                direccion = input("Ingrese la dirección de la sede: ")
                gtu.crear_sede(nombre_sede, direccion)
            case "2":
                nombre_sede = input("Ingrese el nombre de la sede a actualizar: ")
                nueva_direccion = input("Ingrese la nueva dirección de la sede: ")
                gtu.actualizar_sede(nombre_sede, nueva_direccion)
            case "3":
                nombre_sede = input("Ingrese el nombre de la sede a eliminar: ")
                gtu.eliminar_sede(nombre_sede)
            case "4":
                gtu.visualizar_sedes()
                input("Presione una tecla para continuar ")
            case "5":
                gtu.visualizar_carreras_y_cursos()
                input("Presione una tecla para continuar ")
            case "6":
                break
            case _:
                print("Opción no válida.")
        input("\nPresione una 'Enter' para continuar ")

def menu_cursos():
    os.system("cls")
    while True:
        print("""
GESTIÓN DE CURSOS
1) Visualizar cursos de una carrera
2) Agregar curso a estudiante
3) Eliminar curso de estudiante
4) Agregar curso a carrera
5) Actualizar curso en carrera
6) Eliminar curso de carrera
7) Volver al menú principal
""")
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                carrera = input("Ingrese el nombre de la carrera: ")
                gtc.visualizar_cursos(carrera)
            case "2":
                rut_estudiante = input("Ingrese el RUT del estudiante: ")
                curso = input("Ingrese el nombre del curso a agregar: ")
                gtc.agregar_curso_estudiante(rut_estudiante, curso)  
            case "3":
                rut_estudiante = input("Ingrese el RUT del estudiante: ")
                curso = input("Ingrese el nombre del curso a eliminar: ")
                gtc.eliminar_curso_estudiante(rut_estudiante, curso)
            case "4":
                nombre_carrera = input("Ingrese el nombre de la carrera: ")
                curso = input("Ingrese el nombre del curso a agregar a la carrera: ")
                anc.agregar_curso(nombre_carrera, curso)
            case "5":
                nombre_carrera = input("Ingrese el nombre de la carrera: ")
                curso_actual = input("Ingrese el nombre del curso a actualizar: ")
                curso_nuevo = input("Ingrese el nuevo nombre del curso: ")
                anc.actualizar_curso(nombre_carrera, curso_actual, curso_nuevo)
                input("Presione una tecla para continuar ")             
            case "6":
                nombre_carrera = input("Ingrese el nombre de la carrera: ")
                curso = input("Ingrese el nombre del curso a eliminar de la carrera: ")
                anc.eliminar_curso(nombre_carrera, curso)         
            case "7":
                break
            case _:
                print("Opción no válida.")
        input("\nPresione una 'Enter' para continuar ") 

while True:
    os.system("cls")
    print("BIENVENIDO AL SISTEMA DE GESTIÓN DE LA UNIVERSIDAD APLAPLAC - SEDE CONCEPCIÓN")
    options = input(
"""
Menú:
1) Gestión de Estudiantes
2) Gestión de Cursos
3) Gestión Universidad
4) Salir del Sistema
""")

    match options:
        case "1":
            menu_estudiantes()
        case "2":
            opt = input("1) Cursos\n2) Calificaciónes\n")
            match opt:
                case "1":
                    menu_cursos()
                case "2":
                    menu_calificaciones()
        case "3":
            menu_universidad()
        case "4":
            os.system("cls")
            print("SALISTE DEL SISTEMA DE GESTIÓN")
            break
        case _:
            print("Elige una de las opciones válidas.")