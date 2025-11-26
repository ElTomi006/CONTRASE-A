from Funciones.login import acceder_usu, crear_usu


while True:
    print("---------LOGIN DE REGISTRO----------")
    print("1) Iniciar sesión")
    print("2) Crear cuenta")
    print("3) Salir")
    a = int(input(""))



    if a == 1: 
        acceder_usu()

    if a == 2: 
        crear_usu()
    if a == 3: 
        print("Gracias por usar el sistema")
        break
    else:
        print("ERORR")
