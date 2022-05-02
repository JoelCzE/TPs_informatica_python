#TP5 Punto 1 Cruz Joel

from os import system
from time import sleep, time

system("cls")



rta= "si"
while rta != "no":
    

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