import time
import os
from tv import TV

telivision1 = TV("Sony", 56, 7)

while True:
    print(telivision1.estatus_actual())
    print("Control remoto")
    print("1. Encender")
    print("2. Subir Volumen")
    print("3. Bajar Volumen")
    print("4. Cambiar canal")
    boton = input("Presiona un botón: ")
    if boton == "1":
        telivision1.power()
    elif boton == "2":
        telivision1.cambiar_volumen(1)
    elif boton == "3":
        telivision1.cambiar_volumen(-1)

    time.sleep(1)
    print(telivision1.estatus_actual())
    input("Presiona enter para continuar...")
    os.system("clear")


