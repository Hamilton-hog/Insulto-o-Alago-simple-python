import random as rm
import time
import os
import Carga
saludos=["Hola","Qué tal","Aloja","Heyyyy"]
entradaim=["Maldito","Puto","Insignificante","patetico"]
Salidaim=["pedazo de escoria","imbecil","bastardo","tragapapas"]
entradaif=["Maldita","Puta","Inaceptable","Patetica"]
Salidaif=["basura","desgracia","ramera","escoria"]
Nombre=input("Dime tu nombre por favor: ")
os.system ("cls")
time.sleep(3)
print(rm.choice(saludos),Nombre.title())
time.sleep(2)
Num=int(input("¿Te importaria decirme un numero del 1 al 10?: "))
time.sleep(2)
os.system ("cls")
print("Que numero mas interesante...")
time.sleep(3)
os.system ("cls")
print("Con el podria decirte algunas palabras.")
time.sleep(3)
os.system ("cls")
print("Alguna vez te dijieron que...")
time.sleep(3)
os.system ("cls")
Carga.carga()
'''
for i in range(3):
    print(".")
    time.sleep(.5)
    os.system ("cls")
    print("..")
    time.sleep(.5)
    os.system ("cls")
    print("...")
    time.sleep(.5)
    os.system ("cls")
    print("..")
    time.sleep(.5)
    os.system ("cls")
    print(".")
    os.system ("cls")
'''
time.sleep(3)
os.system ("cls")
Gein=rm.randint(1,2)
fim=rm.randint(1,10)
if fim == Num:
    print("Tú:",str(Nombre.title())+", eres una gran persona.")
elif Gein == 1:
    print("Tú:",str(Nombre.title())+", eres un ",rm.choice(entradaim),rm.choice(Salidaim)+".")
elif Gein == 2:
    print("Tú:",str(Nombre.title())+", eres una",rm.choice(entradaif),rm.choice(Salidaif)+".")
time.sleep(3)
os.system ("cls")
print("Que Santan te acompañe, el numero era:",fim)
time.sleep(3)
os.system ("cls")