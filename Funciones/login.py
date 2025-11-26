

from core.Usuario import Usuario_
import bcrypt
from core.base_usu import insertar_usuario, autorizar_ingreso


def crear_usu():
    nombre = input("Ingrese un nombre de usuario: ")
    correo = input("Ingrese un correo: ")
    contraseña = input("Ingrese una contraseña: ")
    contraseña2 = input("Confirme su contraseña: ")
    if contraseña == contraseña2: 
        contraseña = contraseña.encode("UTF-8")
        password = bcrypt.hashpw(contraseña, bcrypt.gensalt())
        print("--------- Se ha registrado correctamente----------")
        El_usuario = Usuario_(nombre,correo,password)
        return insertar_usuario(El_usuario)
    
    
    else: 
        print("No ha sido posible registrar el usuario, intente de nuevo.")
        return None
    

def acceder_usu():
    nombre = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña")
    correo = input("Ingrese su correo electronico")
    autorizar_ingreso(nombre,contraseña,correo)




