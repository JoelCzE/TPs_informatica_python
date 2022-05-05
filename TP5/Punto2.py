#TP5 Punto 1 Cruz Joel

from os import system
from time import sleep

system("cls")

#Declaracion de variables y funciones
def multiplo (a):
    if a % 10 == 0:
        return a
    else:
        while a % 10 != 0:
            a -= 1
        return a

rta= "si"
while rta != "no":
    #Programa principal
    num=0
    while num < 10:
        num= int (input("Ingrese un numero: "))

    print(multiplo(num))

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