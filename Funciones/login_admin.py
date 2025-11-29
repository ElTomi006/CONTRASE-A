
from core.base_usu import crear_usu,mostrar_usus,edit_usu,eliminar_usu
import bcrypt
from Funciones.validador import _validación_de_caracteres, _validacion_de_correo

caracteres = "!-*/_.,+"
numeros = "1234567890"

contraseña = "admin2006"
contraseña2 = input("Ingrese la contraseña: ")

if contraseña2 == contraseña:
    while True: 
        print("-------Menú de Administrador--------")
        print("1) Crear usuario")
        print("2) Editar usuario")
        print("3) Eliminar usuario")
        print("4) Salir")
        respuesta = int(input(""))

        if respuesta == 1: 
            nombre = input("Ingrese el nombre del usuario: ")
            correo = input("Ingrese su correo: ")
            if _validacion_de_correo(correo):
                contraseñA = input("Ingrese una contraseña: ")
                if _validación_de_caracteres(contraseñA) and len(contraseñA) >= 8:
                    contraseña_ = input("Confirme la contraseña: ")
                    if contraseña_ == contraseñA:
                        contraseñA = contraseñA.encode("UTF-8")
                        password = bcrypt.hashpw(contraseñA, bcrypt.gensalt())
                        crear_usu(nombre,correo,password)
                        print("Se ha creado correctamente la cuenta")
            else: 
                if not correo:
                    print("Tu correo debe estar completo con @gmail y con .com")
                
                if not _validación_de_caracteres(contraseñA) or len(contraseñA) >=8:
                    print("Ingrese una contraseña segura")
                    print("- Debe tener 8 caracteres como minimo")
                    print(f"Debe tener {numeros} y {caracteres} ")
                    

        elif respuesta == 2: 
            print("-----Estos son los usuarios------")
            print(mostrar_usus())
            ID = input("Ingrese el id del usuario: ")
            nombre_ = input("Modificar nombre: ")
            correo_ = input("Modificar correo: ")
            contreaseñAA = input("Modificar contraseña: ")
            contreaseñAA = contreaseñAA.encode("UTF-8")
            passsword = bcrypt.hashpw(contreaseñAA, bcrypt.gensalt())
            edit_usu(int(ID), new_name = nombre_, new_gmail = correo_, new_contra = passsword)
        
        elif respuesta == 3: 
            print("-------Estos son los usurios-------")
            print(mostrar_usus())
            Id_ = input("Ingresa el id del usuario: ")
            eliminar_usu(int(Id_))
        elif respuesta == 4: 
            print("Saliendo del sistema....")
            break
        else:
            print("Opción invalida, intentelo de nuevo")

else: 
    print("Contraseña invalida")
                

        
