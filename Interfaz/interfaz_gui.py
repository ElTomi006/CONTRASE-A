import tkinter as tk
from tkinter import ttk, messagebox
from Funciones.login import crear_usu, acceder_usu  


root = tk.Tk()
root.title("Gestión de Usuarios")
root.geometry("400x300")
style = ttk.Style()
style.theme_use("clam")


def mostrar_login():
    login_win = tk.Toplevel(root)
    login_win.title("Iniciar sesión")
    login_win.geometry("300x200")

    ttk.Label(login_win, text="Correo:").pack(pady=5)
    correo = ttk.Entry(login_win)
    correo.pack(pady=5)

    ttk.Label(login_win, text="Contraseña:").pack(pady=5)
    contraseña = ttk.Entry(login_win, show="*")
    contraseña.pack(pady=5)

    def validar_login():
        if acceder_usu(correo.get(), contraseña.get()):
            messagebox.showinfo("Login", " Bienvenido")
        else:
            messagebox.showerror("Login", " Usuario o contraseña incorrecta")

    ttk.Button(login_win, text="Ingresar", command=validar_login).pack(pady=10)


def mostrar_registro():
    reg_win = tk.Toplevel(root)
    reg_win.title("Crear cuenta")
    reg_win.geometry("300x250")

    ttk.Label(reg_win, text="Nombre:").pack(pady=5)
    nombre = ttk.Entry(reg_win)
    nombre.pack(pady=5)

    ttk.Label(reg_win, text="Correo:").pack(pady=5)
    correo = ttk.Entry(reg_win)
    correo.pack(pady=5)

    ttk.Label(reg_win, text="Contraseña:").pack(pady=5)
    contraseña = ttk.Entry(reg_win, show="*")
    contraseña.pack(pady=5)

    ttk.Label(reg_win, text="Confirmar contraseña:").pack(pady=5)
    contraseña2 = ttk.Entry(reg_win, show="*")
    contraseña2.pack(pady=5)

    def registrar_usuario():
        if crear_usu(nombre.get(), correo.get(), contraseña.get(), contraseña2.get()):
            messagebox.showinfo("Registro", "✅ Usuario registrado correctamente")
        else:
            messagebox.showerror("Registro", " Error al registrar usuario")

    ttk.Button(reg_win, text="Registrar", command=registrar_usuario).pack(pady=10)


ttk.Label(root, text="LOGIN DE REGISTRO", font=("Arial", 14)).pack(pady=20)
ttk.Button(root, text="Iniciar sesión", width=25, command=mostrar_login).pack(pady=10)
ttk.Button(root, text="Crear cuenta", width=25, command=mostrar_registro).pack(pady=10)
ttk.Button(root, text="Salir", width=25, command=root.quit).pack(pady=10)

root.mainloop()