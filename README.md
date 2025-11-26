## Sistema de Gestión de Usuarios con Login
Este proyecto implementa un sistema de registro e inicio de sesión de usuarios utilizando Python, SQLite y bcrypt, con dos interfaces disponibles:
- Interfaz por consola: menú interactivo para registrar e iniciar sesión.
- Interfaz gráfica (GUI): construida con Tkinter/ttk, ofrece formularios modernos y mensajes emergentes.

## Características principales
- Registro de usuarios con validación de contraseña.
- Login seguro con verificación de credenciales.
- Contraseñas encriptadas usando bcrypt.
- Base de datos SQLite para persistencia de usuarios.
- Interfaz modular: separación clara entre lógica, base de datos e interfaces.
- Dos modos de uso: consola y GUI.


Estructura del proyecto
CONTRASEÑA/
│
├── core/ 
│   ├── __init__.py                
│   ├── base_usu.py        
│   └── Usuario.py         
│
├── data/                  
│   └── Usuarios.db        
│
├── Funciones/             
│   ├── __init__.py
│   └── login.py           
│
├── Interfaz/              
│   ├── __init__.py
│   ├── inter_consola.py   
│   └── interfaz_Gui.py    
│
├── README.md              
└── requirements.txt       




## Clonar el repositorio:
git clone https://github.com/ElTomi006/CONTRASEÑA.git
cd CONTRASEÑA

## Instalar dependencias:
pip install -r requirements.txt


## Uso
- Ejecutar desde el archico (main.py)
Este archivo permite elegir entre la interfaz por consola o la interfaz gráfica, puede modificar según su elección. Ingrese este codigo en su terminal, para ejecutar el programa:  python main.py

- Ejecutar directamente por consola
python -m Interfaz.inter_consola

- Ejecutar directamente por intefaz
python -m Interfaz.interfaz_gui



## Dependencias
- Python 3.10+
- sqlite3 (incluido en Python)
- bcrypt
- tkinter/ttk


## Autor
- Leonardo Rojas
- rleo5923@gmail.com

