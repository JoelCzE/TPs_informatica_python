#TP5 Punto 1 Cruz Joel

from os import system
from time import sleep

system("cls")

#Declaracion de variables y funciones
def interes (c, x, n):
    return c * (1 + x/100)**n

rta= "si"
while rta != "no":
    #Programa principal
    importe= int (input("Ingrese un importe en pesos: "))
    if importe > 0:
        inter_= float (input("Ingrese una tasa interés: "))
        years= int (input("Ingrese la cantidad de años: "))
        print(f"Su importe ingresado se convertirá en ${interes(importe, inter_, years)} al cabo de {years} años")

    rta= 0
    while rta != "no" and rta != "si":
        rta= input("¿Desea reiniciar el programa? si/no: ")
        rta= rta.lower()

sleep(0.5)        
print("\nFinalizando programa")
for i in "...":
    sleep(1)
    print(i)
sleep(0.5) 