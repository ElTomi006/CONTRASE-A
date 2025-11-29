

from core.Usuario import Usuario_
from core.base_usu import  autorizar_ingreso
  

def acceder_usu():
    nombre = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña")
    correo = input("Ingrese su correo electronico")
    el_usu_ = Usuario_(nombre,contraseña,correo)
    autorizar_ingreso(el_usu_.nombre, el_usu_.contraseña, el_usu_.correo)




