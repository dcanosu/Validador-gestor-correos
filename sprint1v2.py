
# import re

# Expresiones regulares
patron_estudiante = r'^[a-zA-Z0-9._%+-]+@estudiante\.utv\.edu\.co$'
patron_docente = r'^[a-zA-Z0-9._%+-]+@utv\.edu\.co$'
lista_estudiantes = [] # Almacena los correos de los estudiantes
lista_docentes = [] # Almacena los correos de los docentes

def validar_correo(correo):
    return "@" in correo and "." in correo

def registrar():
    """
    Esta función se encarga de registrar un correo realizando la validación de que sea valido y realizando una validación si es un correo
    perteneciente a un estudiante o a un docente donde posteriormente se guarda en la lista correspondiente
    """
    correo = input("Por favor ingrese su correo: ")
    if not validar_correo(correo):
        print("Correo invalido")
        return
    
    if correo.endswith("@estudiante.utv.edu.co"):
        lista_estudiantes.append(correo)
        print("Correo de estudiante agregado con éxito.")
    elif correo.endswith("@utv.edu.co"):
        lista_docentes.append(correo)
        print("Correo de docente agregado con éxito.")
    else:
        print("Correo no pertenece a la institución.")

# def registrar():
#     """
#     Registra un correo validando con expresiones regulares y clasificándolo como estudiante o docente.
#     """
#     correo = input("Por favor ingrese su correo: ").strip()
    
#     if re.match(patron_estudiante, correo):
#         if correo in lista_estudiantes:
#             print("Este correo de estudiante ya está registrado.")
#         else:
#             lista_estudiantes.append(correo)
#             print("Correo de estudiante agregado con éxito.")
#     elif re.match(patron_docente, correo):
#         if correo in lista_docentes:
#             print("Este correo de docente ya está registrado.")
#         else:
#             lista_docentes.append(correo)
#             print("Correo de docente agregado con éxito.")
#     else:
#         print("Correo inválido o no pertenece al dominio institucional.")

def listar():
    """
    Esta función se encarga de listar los correos registrados e indica a que tipo de perfil corresponde, si es estudiante o docente
    """
    if not lista_estudiantes and not lista_docentes:
        print("No hay ningún correo registrado")
        return
    
    for correo in lista_estudiantes:
        print(f"Correo estudiante: {correo}")
    for correo in lista_docentes:
        print(f"Correo docente: {correo}")

def buscar():
    """
    Esta función se encarga de buscar patrones en los correos registrados y muestra los correos y las letras que coinciden en el criterio de busqueda
    """
    if not lista_estudiantes and not lista_docentes:
        print("No hay correos registrados.")
        return

    texto = input("Ingrese parte del correo que desea buscar: ").lower()
    encontrados = False
    for correo in lista_estudiantes + lista_docentes:
        if texto in correo:
            tipo = "estudiante" if correo in lista_estudiantes else "docente"
            print(f"Correo {tipo} '{correo}' contiene '{texto}'")
            encontrados = True
    if not encontrados:
        print("No se encontró ningún correo con ese patrón.")

def menu():
    """
    Esta función se encarga de mostrar el menú hasta que se ingrese un opción válida o se salga del mismo con la opción 4
    """
    while True:
        print("""
        Menú principal
        1. Registrar un nuevo correo electrónico.
        2. Ver correos registrados.
        3. Buscar un correo específico.
        4. Salir de la aplicación
        """)
        try:
            opcion = int(input("Por favor seleccione una opción: "))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            continue
        
        if opcion == 1:
            registrar()
        elif opcion == 2:
            listar()
        elif opcion == 3:
            buscar()
        elif opcion == 4:                 
            print("Muchas gracias por usar el sistema")
            break
        else:
            print("Opcion no válida")

if __name__ == "__main__":
    menu() # Ejecuta el metodo principal