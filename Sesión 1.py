#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Ejercicio 1.
while True:
    try:
        número=int(input("Introduzca número:"))
        print("El número es:",número)
        break
    except ValueError:
        print("Valor incorrecto.")

#Ejercicio 2-Versión 1.
print("Programa para adivinar un número V1.")
import random
def Corrector():
    while True:
        try:
            número=float(input("Introduzca número:"))
            return número
            break
        except ValueError:
            print("Valor incorrecto.")
mínimo=Corrector("Inntroduzca número B:")
máximo=Corrector("Introduzca número A:")
aleatorio=random.randint(mínimo, máximo)
n=Corrector
while True:
    if n==aleatorio:
        print("Has acertado.")
    if n!=aleatorio
        print("Has fallado.")
        
#Ejercicio 2-Versión 2.
print("Programa de adivinar un número V2.")
import random
def Corrector():
    while True:
        try:
            número=float(input("Introduzca número:"))
            return número
            break
        except ValueError:
            print("Valor incorrecto.")
def genera_numero(minimo,maximo):
    aleatorio=random.randint(minimo,maximo)
    return aleatorio
def lee_numero(minimo,maximo):
    mensaje="Introduzca un número del"+" "+str(minimo)+" "+"al"+" "+str(maximo)+":"
    n=int(input(mensaje))
    return n
def comprueba_numero(aleatorio,n):
    if n==aleatorio:
        print("Has acertado.")
        acertado=True
    elif aleatorio>n:
        print("Elija un número mayor.")
        acertado=False
    else:
        print("Elija un número menor.")
        acertado=False
    return acertado
def Finalizar():
    print("¿Quiere continuar?")
    r=input("SI o NO:").upper()
    if r=="SI":
        print("Entendido.")
    if r=="NO":
        print("Programa ha finalizado")
        p=False
    return p
p=True        
while p==True:
    minimo=int(input("Introduzca el mínimo:"))
    maximo=int(input("introduzca el máximo:"))
    aleatorio=genera_numero(minimo, maximo)
    acertado=False
    while acertado==False:
        n=lee_numero(minimo, maximo)
        acertado=comprueba_numero(aleatorio, n)
    p=Finalizar()    

