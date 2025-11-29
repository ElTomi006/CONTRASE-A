import tkinter as tk
from tkinter import ttk, messagebox
import bcrypt
# Asegúrate de importar tu validador de correo aquí:
from core.base_usu import crear_usu, edit_usu, eliminar_usu, mostrar_usus, autorizar_ingreso
import ttkbootstrap as tb
from Funciones.validador import _validación_de_caracteres, _validacion_de_correo  # <-- ¡Añadido!

ADMIN_PASS = "admin2006"

root = tb.Window(themename="superhero")
root.title("🔐 Sistema de Login")
root.geometry("700x500")
root.resizable(False, False)

# Frames
frame_inicio = ttk.Frame(root)
frame_login_usuario = ttk.Frame(root)
frame_login_admin = ttk.Frame(root)
frame_menu_admin = ttk.Frame(root)

for f in (frame_inicio, frame_login_usuario, frame_login_admin, frame_menu_admin):
    f.place(relwidth=1, relheight=1)

def mostrar_frame(f):
    f.tkraise()

# ----- INICIO -----
ttk.Label(frame_inicio, text="Bienvenido 👋", font=("Segoe UI", 20, "bold")).pack(pady=30)
ttk.Button(frame_inicio, text="👤 Login Usuario", command=lambda: mostrar_frame(frame_login_usuario)).pack(pady=10)
ttk.Button(frame_inicio, text="🛠️ Login Administrador", command=lambda: mostrar_frame(frame_login_admin)).pack(pady=10)

# ----- LOGIN USUARIO -----
ttk.Label(frame_login_usuario, text="Login Usuario", font=("Segoe UI", 16, "bold")).pack(pady=20)

entry_nombre = ttk.Entry(frame_login_usuario)
entry_correo = ttk.Entry(frame_login_usuario)
entry_contra = ttk.Entry(frame_login_usuario, show="*")

ttk.Label(frame_login_usuario, text="Nombre").pack()
entry_nombre.pack()
ttk.Label(frame_login_usuario, text="Correo").pack()
entry_correo.pack()
ttk.Label(frame_login_usuario, text="Contraseña").pack()
entry_contra.pack()


def login_usuario():
    # Podrías añadir validación de correo aquí también si quieres más seguridad
    if not _validacion_de_correo(entry_correo.get()):
        messagebox.showerror("Error", "Formato de correo inválido 📧.")
        return
        
    autorizar_ingreso(entry_nombre.get(), entry_contra.get(), entry_correo.get())
    # Asumo que 'autorizar_ingreso' maneja si el login fue exitoso o no con un mensaje
    

ttk.Button(frame_login_usuario, text="✅ Acceder", command=login_usuario).pack(pady=10)
ttk.Button(frame_login_usuario, text="↩️ Volver", command=lambda: mostrar_frame(frame_inicio)).pack()

# ----- LOGIN ADMIN -----
ttk.Label(frame_login_admin, text="Contraseña Admin", font=("Segoe UI", 16, "bold")).pack(pady=20)
entry_admin = ttk.Entry(frame_login_admin, show="*")
entry_admin.pack()


def login_admin():
    # MEJORA: Recordatorio de seguridad: La contraseña ADMIN_PASS NUNCA debe ser texto plano en código.
    if entry_admin.get() == ADMIN_PASS:
        mostrar_frame(frame_menu_admin)
    else:
        messagebox.showerror("Error", "Contraseña incorrecta ❌")


ttk.Button(frame_login_admin, text="✅ Acceder", command=login_admin).pack(pady=10)
ttk.Button(frame_login_admin, text="↩️ Volver", command=lambda: mostrar_frame(frame_inicio)).pack()


# ---------------- MENÚ ADMIN ----------------
ttk.Label(frame_menu_admin, text="Menú Administrador 🛠️", font=("Segoe UI", 18, "bold")).pack(pady=20)

# ---------- CREAR USUARIO ----------
def crear_usuario():
    cu = tk.Toplevel(root)
    cu.title("➕ Crear Usuario")
    cu.geometry("300x350")
    cu.grab_set() # Bloquea la ventana principal

    ttk.Label(cu, text="Nombre").pack(pady=5)
    nombre = ttk.Entry(cu)
    nombre.pack()

    ttk.Label(cu, text="Correo").pack(pady=5)
    correo = ttk.Entry(cu)
    correo.pack()

    ttk.Label(cu, text="Contraseña").pack(pady=5)
    contra = ttk.Entry(cu, show="*")
    contra.pack()

    ttk.Label(cu, text="Confirmar contraseña").pack(pady=5)
    contra2 = ttk.Entry(cu, show="*")
    contra2.pack()

    def guardar():
        # Validaciones
        nombre_val = nombre.get().strip()
        correo_val = correo.get().strip()
        
        if not nombre_val or not correo_val or not contra.get():
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        # 1. Validación de Correo (¡NUEVO!)
        if not _validacion_de_correo(correo_val):
            messagebox.showerror("Error de Correo", "El formato del correo es inválido 📧.")
            return

        # 2. Validación de Coincidencia de Contraseña
        if contra.get() != contra2.get():
            messagebox.showerror("Error", "Las contraseñas no coinciden ❌")
            return
        
        # 3. Validación de Fortaleza de Contraseña
        if not _validación_de_caracteres(contra.get()) or len(contra.get()) < 8:
            messagebox.showerror(
                "Contraseña débil",
                "La contraseña debe tener:\n- Mínimo 8 caracteres\n- Letras, números y caracteres especiales (!-*/_.,+)"
            )
            return
        
        # Procesamiento y Guardado
        try:
            password_hash = bcrypt.hashpw(contra.get().encode("UTF-8"), bcrypt.gensalt())
            crear_usu(nombre_val, correo_val, password_hash)
            messagebox.showinfo("Éxito", "Usuario creado correctamente ✅")
            cu.destroy()
        except Exception as e:
             messagebox.showerror("Error DB", f"No se pudo crear el usuario. Error: {e}")


    ttk.Button(cu, text="💾 Guardar", command=guardar).pack(pady=10)


# ---------- EDITAR USUARIO ----------
def editar_usuario():
    eu = tk.Toplevel(root)
    eu.title("✏️ Editar Usuario")
    eu.geometry("300x350")
    eu.grab_set()

    ttk.Label(eu, text="ID Usuario").pack(pady=5)
    ID = ttk.Entry(eu)
    ID.pack()

    ttk.Label(eu, text="Nuevo Nombre").pack(pady=5)
    nombre = ttk.Entry(eu)
    nombre.pack()

    ttk.Label(eu, text="Nuevo Correo").pack(pady=5)
    correo = ttk.Entry(eu)
    correo.pack()

    ttk.Label(eu, text="Nueva Contraseña").pack(pady=5)
    contra = ttk.Entry(eu, show="*")
    contra.pack()

    def guardar():
        # MEJORA: Manejo de errores al convertir ID a int
        try:
            id_usuario = int(ID.get().strip())
        except ValueError:
            messagebox.showerror("Error de ID", "El ID del usuario debe ser un número entero válido 🔢.")
            return
        
        correo_nuevo = correo.get().strip()
        
        # 1. Validación de Correo (¡NUEVO!)
        if correo_nuevo and not _validacion_de_correo(correo_nuevo):
            messagebox.showerror("Error de Correo", "El formato del correo es inválido 📧.")
            return
            
        password_hash = None
        
        # 2. Validación si se cambia contraseña
        if contra.get().strip():
            if not _validación_de_caracteres(contra.get()) or len(contra.get()) < 8:
                messagebox.showerror(
                    "Contraseña débil",
                    "Debe tener 8+ caracteres, números, letras y un carácter especial."
                )
                return
            password_hash = bcrypt.hashpw(contra.get().encode("UTF-8"), bcrypt.gensalt())
        
        # Guardado
        try:
            edit_usu(
                id_usuario, 
                new_name=nombre.get().strip(), 
                new_gmail=correo_nuevo, 
                new_contra=password_hash
            )
            messagebox.showinfo("Éxito", "Usuario editado correctamente ✨")
            eu.destroy()
        except Exception as e:
            messagebox.showerror("Error DB", f"No se pudo editar el usuario. Error: {e}")

    ttk.Button(eu, text="💾 Guardar", command=guardar).pack(pady=10)


# ---------- ELIMINAR USUARIO ----------
def eliminar_usuario_gui():
    eu = tk.Toplevel(root)
    eu.title("🗑️ Eliminar Usuario")
    eu.geometry("250x150")
    eu.grab_set()

    ttk.Label(eu, text="ID Usuario").pack()
    ID = ttk.Entry(eu)
    ID.pack()

    def borrar():
        # MEJORA: Manejo de errores al convertir ID a int
        try:
            id_usuario = int(ID.get().strip())
        except ValueError:
            messagebox.showerror("Error de ID", "El ID del usuario debe ser un número entero válido 🔢.")
            return
            
        try:
            eliminar_usu(id_usuario)
            messagebox.showinfo("Éxito", f"Usuario con ID {id_usuario} eliminado correctamente 🗑️")
            eu.destroy()
        except Exception as e:
            messagebox.showerror("Error DB", f"No se pudo eliminar el usuario. Error: {e}")

    ttk.Button(eu, text="Eliminar", command=borrar).pack(pady=10)


# ---------- MOSTRAR USUARIOS ----------
# MEJORA: Limpiar la tabla antes de volver a llenarla
def mostrar_usus_gui():
    
    # Busca si ya existe la tabla para eliminarla o limpiarla
    for widget in frame_menu_admin.winfo_children():
        if isinstance(widget, ttk.Treeview):
            widget.destroy()
            break # Solo debería haber uno

    users = mostrar_usus()
    
    tabla = ttk.Treeview(frame_menu_admin, columns=("ID","Nombre","Correo"), show="headings", height=8)
    
    # Definir el ancho de las columnas
    tabla.column("ID", width=40, anchor="center")
    tabla.column("Nombre", width=150, anchor="w")
    tabla.column("Correo", width=250, anchor="w")
    
    tabla.heading("ID", text="ID")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Correo", text="Correo")

    tabla.pack(pady=10, fill="x", padx=20)

    for u in users:
        # Nota: Asumo que u[0], u[1], u[2] son ID, Nombre, y Correo, respectivamente
        tabla.insert("", "end", values=(u[0], u[1], u[2]))


# Recreación de botones para mantener la tabla en el centro después de la lista
ttk.Button(frame_menu_admin, text="➕ Crear Usuario", command=crear_usuario).pack(pady=5)
ttk.Button(frame_menu_admin, text="✏️ Editar Usuario", command=editar_usuario).pack(pady=5)
ttk.Button(frame_menu_admin, text="🗑️ Eliminar Usuario", command=eliminar_usuario_gui).pack(pady=5)
ttk.Button(frame_menu_admin, text="📋 Mostrar Usuarios", command=mostrar_usus_gui).pack(pady=5)
ttk.Button(frame_menu_admin, text="↩️ Cerrar sesión", command=lambda: mostrar_frame(frame_inicio)).pack(pady=20)

mostrar_frame(frame_inicio)
root.mainloop()