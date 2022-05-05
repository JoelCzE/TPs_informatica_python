#TP5 Punto 1 Cruz Joel

from os import system
from re import M
from time import sleep

system("cls")

#Declaracion de variables y funciones
def factorial (a):
    for i in range(1, a):
        a= a*i
    return a

rta= "si"
while rta != "no":
    #Programa principal
    m= int (input("Ingrese la cantidad de valores que desea ingresar: "))
    for i in range(0, m):
        val= int (input("Ingrese un número para calcular su factorial: "))
        print(f"{val}: {factorial(val)} y su numero de orden es {i+1}")

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