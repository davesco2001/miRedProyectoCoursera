#Hola.
#En esta ocasiÃ³n vamos a continuar con el cÃ³digo de nuestra red social,
#al cual le habÃ­amos agregado un menÃº.
#
#El programa de la semana anterior permitÃ­a:
#1. Obtener datos del usuario
#2. Consultar y mostrar varios mensajes de estado del usuario
#3. Escoger entre distintas acciones que el usuario puede realizar
#

#Si lograste agregar una opciÃ³n nueva al sistema, por ejemplo, para escribir los datos
#del perfil del usuario, habrÃ¡s notado que tienes que escribir de nuevo el cÃ³digo necesario
#con un print por cada dato. El cÃ³digo se verÃ­a como estÃ¡ mÃ¡s abajo.

#Nuevos metodos
def set_nombre(nombre):
    return print("Hola ", nombre, ", bienvenido a Mi Red")
def set_edad(agno):
    return 2021-agno-1
def estatura_metros(estatura):
    return int(estatura)
def estatura_cm(estatura, estatura_m):
    return int((estatura - estatura_m) * 100)
def publicar_perfil(agno,estatura, nombre, num_amigos):
    print("--------------------------------------------------")
    print("Nombre:  ", nombre)
    print("Edad:    ", set_edad(agno), "años")
    print("Estatura:", estatura_metros(estatura), "metros y", estatura_cm(estatura, estatura_metros(estatura)), "centímetros")
    print("Amigos:  ", num_amigos)
    print("--------------------------------------------------")

print("Bienvenido a ... ")
print("""
              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \/ /  / ___/ _ \/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \___/\__,_/

""")

# Solicitud de nombre
nombre = input("Para empezar, dime como te llamas. ")
print()
set_nombre(nombre)
print()

# CÃ¡lculo de edad
agno = int(input("Para preparar tu perfil, dime en quÃ© aÃ±o naciste. "))
print(set_edad(agno))

# CÃ¡lculo de estatura
estatura = float(input("Cuentame más de ti, para agregarlo a tu perfil. ¿Cuanto mides? Dímelo en metros. "))

# Cantidad de amigos
num_amigos = int(input("Muy bien. Finalmente, cuÃ©ntame cuantos amigos tienes. "))

#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
publicar_perfil(agno, estatura, nombre, num_amigos)
print("Gracias por la información. Esperamos que disfrutes con Mi Red")
print()

#Esta opcion permite entrar al ciclo. Solo interesa que no sea 0.
opcion = 1
while opcion != 0:
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje público")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opción: "))

    #CÃ³digo para la opciÃ³n 1. Publicar un mensaje.
    if opcion == 1:
        mensaje = input("Ahora vamos a publicar un mensaje. ¿Qué piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")

    #CÃ³digo para la opciÃ³n 2. Publicar un mensajes a un grupo de personas.
    elif opcion == 2:
        mensaje = input("Ahora vamos a publicar un mensaje a un grupo de amigos. ¿Qué quieres decirles? ")
        print()
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            print("--------------------------------------------------")
            print(nombre, "dice:", "@"+nombre_amigo, mensaje)
            print("--------------------------------------------------")

    #CÃ³digo para la opciÃ³n 3. Publicar los datos del perfil del usuario.
    elif opcion == 3:
        publicar_perfil(agno, estatura, nombre, num_amigos)

    #CÃ³digo para la opciÃ³n 4. Actualizar los datos del perfil del usuario.
    elif opcion == 4:
        #Repetimos el cÃ³digo para solicitar datos
        # Solicitud de nombre
        nombre = input("Para empezar, dime como te llamas. ")
        print()
        set_nombre(nombre)
        print()
        # CÃ¡lculo de edad
        agno = int(input("Para preparar tu perfil, dime en quÃ© aÃ±o naciste. "))
        set_edad(agno)
        print()
        # CÃ¡lculo de estatura
        estatura = float(input("CuÃ©ntame mÃ¡s de ti, para agregarlo a tu perfil. Â¿CuÃ¡nto mides? DÃ­melo en metros. "))
        # Cantidad de amigos
        num_amigos = int(input("Muy bien. Finalmente, cuÃ©ntame cuantos amigos tienes. "))
        print()
        print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
        # Repetimos el cÃ³digo para mostrar los datos del usuario.
        publicar_perfil(agno, estatura, nombre, num_amigos)
        print()

    #CÃ³digo para la opciÃ³n 0. Salir.
    elif opcion == 0:
        print("Has decidido salir.")

    #CÃ³digo para la opciÃ³n que no coincida con ninguna anterior.
    else:
        print("No conozco la opción que has ingresado. Intentalo otra vez.")

print()
print("Gracias por usar Mi Red. ¡Hasta pronto!")
print()

#Si pruebas este cÃ³digo, verÃ¡s que funciona correctamente, pero nuestro programa ahora es bastante largo.
#Casi 140 lÃ­neas.
#Esto en sÃ­ no es malo. Sin embargo, si le pones atenciÃ³n, verÃ¡s que hay cÃ³digo que hemos tenido
#que repetir completamente. Por ejemplo, el cÃ³digo para mostrar el perfil de un usuario estÃ¡ escrito tres veces.
#Si ahora queremos agregar un nuevo dato del usuario, por ejemplo, el paÃ­s en que vive, debemos modificar
#al menos tres partes distintas del programa.
#Esto lo podemos hacer, talvez sin cometer errores, en un programa pequeÃ±o como Ã©ste.
#Pero en programas mÃ¡s grandes, es muy fÃ¡cil que nos olvidemos de actualizar una parte del cÃ³digo,
#o que no recordemos todas las partes que hay que modificar.

#Cuando tenemos instrucciones que se repiten tantas veces en distintas partes del programa,
# es una indicaciÃ³n de que talvez necesitamos agregar funciones.

#Te invitamos a pensar en al menos 3 alternativas o funcionalidades de este cÃ³digo
#que podrÃ­an convertirse en una funciÃ³n.