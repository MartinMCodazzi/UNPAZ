# -*- coding: utf-8 -*-

palabraMaspeque="treintagggggggggggg"
palMasLarga=""

while True:
    n1=input("ingresa una palabra o escribe ´FIN´ para finalizar: ").strip()
    if n1.upper()=="FIN":
        break
    if len(n1)<len(palabraMaspeque):
        palabraMaspeque=n1
    if len(n1)>len(palMasLarga):
        palMasLarga=n1

print("la palabra:",palabraMaspeque,"es la mas pequeña con", len(palabraMaspeque), "letras")
print("la palabra:",palMasLarga,"es la mas extensa con", len(palMasLarga), "letras")