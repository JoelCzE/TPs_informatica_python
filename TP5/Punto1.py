#TP5 Punto 1 Cruz Joel

from email.mime import base
from os import system
from re import A
from time import sleep, time

system("cls")

#Declaracion de variables y funciones

def calc_area (x, t):
    print("El area de la figura es:", x * t)

def calc_perimetro (a, b):
    print("El perimetro es:", a + a + b + b)

rta= "si"
while rta != "no":
    #Programa principal
    base= float( input("Ingrese el valor de la base: "))
    altura= float( input("Ingrese el valor de la altura: "))
    rta_area= calc_area(base, altura)
    rta_perimetro= calc_perimetro(base, altura)

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