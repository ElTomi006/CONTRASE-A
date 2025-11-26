
import sqlite3
import bcrypt


conn = sqlite3.connect('Usuarios.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        correo TEXT UNIQUE NOT NULL,
        contraseña BLOB NOT NULL
    )
""")
conn.commit()
conn.close()

def insertar_usuario(nombre, correo, contraseña_hash):
    conn = sqlite3.connect("Usuarios.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, correo, contraseña) VALUES (?, ?, ?)",
                   (nombre, correo, contraseña_hash))
    conn.commit()
    conn.close()

def autorizar_ingreso(nombre,contraseña,correo):
    conn = sqlite3.connect("Usuarios.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT contraseña FROM usuarios WHERE = ?",(correo,))
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

    



