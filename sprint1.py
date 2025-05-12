import re

lista_estudiantes = [] # Almacena los correos de los estudiantes
lista_docentes = [] # Almacena los correos de los docentes

def imprimir_titulo(texto):
    print("\n" + "=" * 50)
    print(f"{texto.center(50)}")
    print("=" * 50 + "\n")


def menu_principal():
    """
    Esta función se encarga de mostrar el menú hasta que se ingrese un opción válida por el usuario, 
    el ciclo se repite hasta que se seleccione la opción 4 (salir).
    """
    while True:
        imprimir_titulo("MENÚ PRINCIPAL")
        menu = """
        1. Registrar un nuevo correo electrónico.
        2. Ver correos registrados.
        3. Buscar un correo específico.
        4. Salir de la aplicación
        """
        print(menu)
        try:
            opcion = int(input("Por favor seleccione una opción: "))
        except ValueError:
            print("❌ Entrada inválida, por favor ingrese un número [1-4]")
            continue
        
        if opcion not in range(1, 5):
            print("❌ Opción inválida, por favor ingrese un número [1-4]")
            continue
        
        if opcion == 1:
            registrar()
        elif opcion == 2:
            listar()
        elif opcion == 3:
            buscar()
        elif opcion == 4:                 
            print("\n👋 Muchas gracias por utilizar nuestro sistema")
            break
            
def registrar():
    """
    Esta función se encarga de registrar un correo realizando la validación de que sea valido y realizando una validación si es un correo
    perteneciente a un estudiante o a un docente donde posteriormente se guarda en la lista correspondiente
    """
    correo = input("📧 Por favor ingrese su correo: ").strip().lower()
    
    if correo in lista_estudiantes or correo in lista_docentes:
        print("⚠️ Ese correo ya está registrado.")
        return
    
    # Esto → [\w\.-] es equivalente a esto → [a-zA-Z0-9._%+-]
    patron_estudiante = r'^[a-zA-Z0-9._%+-]+@estudiante\.utv\.edu\.co$'
    patron_docente = r'^[a-zA-Z0-9._%+-]+@utv\.edu\.co$'
    
    if re.match(patron_estudiante, correo):
        lista_estudiantes.append(correo)
        print("✅ Correo de estudiante agregado con éxito")
    elif re.match(patron_docente, correo):
        lista_docentes.append(correo)
        print("✅ Correo de docente agregado con éxito")
    else:
        print("❌ Correo inválido. Verifique el dominio.")


def listar():
    """
    Esta función se encarga de listar los correos registrados e indica a que tipo de perfil corresponde, si es estudiante o docente
    """
    # if len(lista_estudiantes) == 0 and len(lista_docentes) == 0:
    if not lista_estudiantes and not lista_docentes:
        print("📭 No hay ningún correo registrado")
        return
    
    if lista_estudiantes:
        imprimir_titulo("CORREO DE ESTUDIANTES")
        for correo in (lista_estudiantes):
            print(f"📘 Estudiante → {correo}")

    if lista_docentes:
        imprimir_titulo("CORREOS DE DOCENTES")
    for correo in (lista_docentes):
        print(f"📗 Docente → {correo}")


def buscar():
    """
    Esta función se encarga de buscar patrones en los correos registrados y muestra los correos y las letras que coinciden en el criterio de busqueda
    """
    # if len(lista_estudiantes) == 0 and len(lista_docentes) == 0:
    if not lista_estudiantes and not lista_docentes:
        print("📭 No hay ningún correo registrado")
        return
    
    correo_buscar = input("🔍 Por favor ingrese parte del correo que desea buscar: ").strip().lower()
    if not correo_buscar:
        print("⚠️ No ingresó ningún criterio de búsqueda.")
        return
    
    encontrados = False # Bandera para saber si se encontró algo
    print("\n🔎 Resultados de la búsqueda:\n")
    
    for correo in lista_estudiantes:
        if correo_buscar in correo:
            print(f"📘 El correo estudiante {correo} contiene la parte '{correo_buscar}'")
            encontrados = True
            
    for correo in lista_docentes:
        if correo_buscar in correo:
            print(f"📗 El correo docente {correo} contiene la parte '{correo_buscar}'")
            encontrados = True
    
    if not encontrados:
        print(f"❌ No se encontró ningún correo que contenga '{correo_buscar}'")


if __name__ == "__main__":
    menu_principal() # Ejecuta el metodo principal