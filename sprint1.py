"""
def menu:
Esta función se encarga de mostrar el menú hasta que se ingrese un opción válida o se salga del mismo con la opción 4
"""

def menu():
    while True:
        menu = """
        Menú principal
        1. Registrar un nuevo correo electrónico.
        2. Ver correos registrados.
        3. Buscar un correo específico.
        4. Salir de la aplicación
        """
        print(menu)
        opcion = int(input("Por favor seleccione una opción: "))
        if opcion == 1:
            registrar()
        elif opcion == 2:
            listar()
        elif opcion == 3:
            buscar()
        elif opcion == 4:                 
            print("Muchas gracias por utilizar nuestro sistema")
            break
        else:
            print("Opcion no valida, por favor ingrese una opción correcta")

lista_estudiantes = [] # Almacena los correos de los estudiantes
lista_docentes = [] # Almacena los correos de los docentes

"""
def registrar:
Esta función se encarga de registrar un correo realizando la validación de que sea valido y realizando una validación si es un correo
perteneciente a un estudiante o a un docente donde posteriormente se guarda en la lista correspondiente
"""
def registrar():
    correo = input("Por favor ingrese su correo: ")
    if "@" in correo and "." in correo:
        if correo.endswith("@estudiante.utv.edu.co"):
            lista_estudiantes.append(correo)
            print("Correo agregado con éxito: ")
        elif correo.endswith("@utv.edu.co"):
            lista_docentes.append(correo)
            print("Correo agregado con éxito: ")
        else:
            print("Correo invalido")
    else:
        print("Correo invalido")

"""
def listar:
Esta función se encarga de listar los correos registrados e indica a que tipo de perfil corresponde, si es estudiante o docente
"""
def listar():
    if len(lista_estudiantes) == 0 and len(lista_docentes) == 0:
        print("No hay ningún correo registrado")
    else:
        for i in range(len(lista_estudiantes)):
            print(f"Correo estudiante {lista_estudiantes[i]}")
        for i in range(len(lista_docentes)):
            print(f"Correo docente {lista_docentes[i]}")

"""
def buscar:
Esta función se encarga de buscar patrones en los correos registrados y muestra los correos y las letras que coinciden en el criterio de busqueda
"""
def buscar():
    if len(lista_estudiantes) == 0 and len(lista_docentes) == 0:
        print("No hay ningún correo registrado")
    else:
        correo_buscar = input("Por favor ingrese el correo que desea buscar: ")
        for correo in lista_estudiantes:
            if correo_buscar in correo:
                print(f"El correo estudiante {correo} contiene la parte '{correo_buscar}'")
        for correo in lista_docentes:
            if correo_buscar in correo:
                print(f"El correo docente {correo} contiene la parte '{correo_buscar}'")


if __name__ == "__main__":
    menu() # Ejecuta el metodo principal