import os 

interfaz = "Gui"

if interfaz == "Gui":
    os.system("python -m Interfaz.interfaz_gui")
elif interfaz == "Consola":
    os.system("python -m Interfaz.inter_consola")