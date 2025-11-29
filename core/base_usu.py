
import sqlite3
import bcrypt


conn = sqlite3.connect('Usuarios.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        correo TEXT UNIQUE NOT NULL,
        contraseña BLOB NOT NULL
    )
""")
conn.commit()
conn.close()



def autorizar_ingreso(nombre,contraseña,correo):
    conn = sqlite3.connect("Usuarios.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT contraseña FROM Usuarios WHERE nombre = ? AND correo= ?", (nombre,correo))
    resultado = cursor.fetchone()
    conn.close()

    if resultado: 
        contraseña_hash = resultado[0]
        if bcrypt.checkpw(contraseña.encode("UTF-8"), contraseña_hash):
            print("Vienvenido")
        else: 
            print("Contraseña incorrecta, vuelvalo a intentar")
    else:
        print("Usuario no encontrado")


def crear_usu(nombre,contraseña,correo):
    conn = sqlite3.connect(f"Usuarios.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Usuarios (nombre, correo, contraseña) VALUES (?,?,?)",
                   (nombre, correo, contraseña))
    
    conn.commit()
    conn.close()

  



def Usuario_s():
    conn = sqlite3.connect("Usuarios.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, correo, contraseña FROM Usuarios")
    users = cursor.fetchall()
    conn.close()
    return users


def edit_usu(Id,new_name = None,new_gmail = None, new_contra = None ):
    conn = sqlite3.connect("Usuarios.db")
    cursor = conn.cursor()
    if new_gmail:
        cursor.execute("UPDATE Usuarios SET correo = ? WHERE id = ?", (new_gmail,Id))
    if new_name: 
        cursor.execute("UPDATE Usuarios SET nombre = ?, WHERE id = ?", (new_name,Id))
    if new_contra: 
        cursor.execute("UPDATE Usuarios SET contraseña = ? WHERE id = ?", (new_contra,Id))
    
    conn.commit()
    print("Se ha modificado correctamente al usuario")
    conn.close()


def eliminar_usu(Id_usu):
    conn = sqlite3.connect("Usuarios.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Usuarios WHERE id = ?", (Id_usu,))
 
    conn.commit()
    print("Usuario eliminado correctamente")
    conn.close()
    


__usu = Usuario_s()


def mostrar_usus():
    conn = sqlite3.connect("Usuarios.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, correo FROM Usuarios")
    usu = cursor.fetchall()
    conn.close()
    return usu





    




