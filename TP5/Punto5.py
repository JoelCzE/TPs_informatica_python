#TP5 Punto 1 Cruz Joel

from ast import If
from os import system
from time import sleep

system("cls")

#Declaracion de variables y funciones
def menu ():
    print("a - Calcular el cociente de dos números enteros siempre que sea posible.")
    print("b - Determinar si un número es primo.")
    print("c - Ingrese un número entre 0 y 10 muestre dicho valor en letras.")
    print("d - Dados dos números distintos de cero, indica cual es el mayor")
    print("e - Finaliza el programa")
    a = input ("Ingrese la opcion que desea ejecutar: ")
    return a

def cociente ():
    a= int(input("Ingrese el dividendo: "))
    b= int(input("Ingrese el divisor: "))
    return a/b

def primo ():
    a = int (input("Ingrese un numero entero para saber si es primo o no: "))
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

def num_word ():
    a= int (input ("Ingrese un numero del 0 al 10: "))
    if a == 0:
        a= "Cero"
    elif a == 1:
        a= "Uno"
    elif a == 2:
        a= "Dos"
    elif a == 3:
        a= "Tres"
    elif a == 4:
        a= "Cuatro"
    elif a == 5:
        a= "Cinco"
    elif a == 6:
        a= "Seis"
    elif a == 7:
        a= "Siete"
    elif a == 8:
        a= "Ocho"
    elif a == 9:
        a= "Nueve"
    elif a == 10:
        a= "Diez"
    return a
def major ():
    a= int (input("Ingrese el valor para a: "))
    b= int (input("Ingrese el valor para b: "))
    if a != 0 and b != 0:
        if b > a:
            a= b
            return a
        return a

rta= "si"
while rta != "no":
    #Programa principal
    system("cls")
    op= menu()
    if op != "e":
        if op == "a":
            print()
        if op == "b":
            print(primo())
        if op == "c":
            print(num_word())
        if op == "d":
            print(major())
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