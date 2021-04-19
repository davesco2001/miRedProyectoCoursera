def mostrar_bienvenida():
    print("Bienvenido a ... ")
    print("""
                  _                  __
       ____ ___  (_)  ________  ____/ /
      / __ `__ \/ /  / ___/ _ \/ __  /
     / / / / / / /  / /  /  __/ /_/ /
    /_/ /_/ /_/_/  /_/   \___/\__,_/

    """)

def obtener_nombre():
    nombre = input("Para empezar, dime como te llamas. ")
    return nombre

def obtener_edad():
    agno = int(input("Para preparar tu perfil, dime en que año naciste. "))
    return 2021-agno-1

def obtener_estatura():
    estatura = float(input("Cuentame mas de ti, para agregarlo a tu perfil. ¿Cuanto mides? Dimelo en metros. "))
    metros = int(estatura)
    centimetros = int( (estatura - metros)*100 )
    return (metros, centimetros)

def obtener_sexo():
    sexo = input("Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ")
    while sexo != 'M' and sexo != 'F':
        sexo = input("Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ")
    return sexo

def obtener_pais():
    pais = input("Indica tu pais de nacimiento: ")
    return pais

def obtener_num_amigos():
    amigos = int(input("Muy bien. Finalmente, cuentame cuantos amigos tienes. "))
    return amigos

def obtener_datos():
    n = obtener_nombre()
    e = obtener_edad()
    (em, ec) = obtener_estatura()
    na = obtener_num_amigos()
    return (n,e,em,ec,na)

def mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos):
    print("--------------------------------------------------")
    print("Nombre:   ", nombre)
    print("Edad:     ", edad, "años")
    print("Estatura: ", estatura_m, "m y ", estatura_cm, "centimetros")
    print("Sexo:     ", sexo)
    print("Pais:     ", pais)
    print("Amigos:   ", num_amigos)
    print("--------------------------------------------------")

def opcion_menu():
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje publico")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opcion: "))
    while opcion < 0 or opcion > 4:
        print("No conozco la opcion que has ingresado. Intentalo otra vez.")
        opcion = int(input("Ingresa una opcion: "))
    return opcion

def obtener_mensaje():
    mensaje = input("Ahora vamos a publicar un mensaje. ¿Que piensas hoy? ")
    return mensaje

def mostrar_mensaje(origen, destinatario, mensaje):
    print("--------------------------------------------------")
    if destinatario == None:
        print(origen, "dice:", mensaje)
    else:
        print(origen, "dice:", "@"+destinatario, mensaje)
    print("--------------------------------------------------")
