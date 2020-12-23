#!/usr/bin/env python3

#creador:https://www.facebook.com/TheNinjaBlack2
#patron conocido : 8 caracteres,numeros del 0-9,letras:A-Z mayusculas
#si mejoras el codigo,me lo pasas y asi compartimos,no olvides darme una sugerencia o lo que sea
#el generador aun esta en fase beta digamos,se que debo mejorarle muchas cosas
#el generador genera un millon de posibles contrasenas,o cancelas el proceso con ctrl+c
#en esta ocasion mientras este funcionado el generador,se imprimira en pantalla las contrasenas que se este generando
#si no tienes python3 instalado en linux,sudo apt-get install python3
#si usas arch linux o no encuentras el paquete xzm de python3 en wifislax ve ha https://www.python.org/ftp/python/3.4.2/Python-3.4.2rc1.tar.xz
#lo descomprimes,vas hacia la carpeta,cd Desktop/x ; ./configure ; make ; make install , luego teclea en la terminal python3
#testeado en backtrack 5 r3,wifislax 4.9 final , manjaro arch linux 
#editor usado notepad++ si usas linux,hay varios,como : Scite,notepadQQ,notepad++ usando wine,sublime_text , gedit,eric ide project,atom,brackets,etc
from random import choice
import sys
import os
from string import ascii_letters , digits

pl = sys.platform
if pl == "linux" or pl  == "linux2":
    os.system('clear')
elif pl == "win32":
    os.system('cls')
else:
   print ("si usas mac,lo ciento,no me gustan las manzanas,prefiero las zanahorias")
print ("""
1-python3 generador_JAZZTEL_XX.py 
2-python3 generador_JAZZTEL_XX.py creador 
""")
if 'creador' in sys.argv:
    print ('https://www.facebook.com/TheNinjaBlack2')
    exit(0)    
nombre = str(input("Escribe la extencion que deseas para el diccionario , 'lts' o 'txt':"))
caracteres = ascii_letters + digits
mayus = caracteres.upper()
def generator(subir):
    file = open("diccionario."+nombre,'w')
    for i in range(1000000):
        final = ''.join([choice (subir) for i in range(8)])
        file.writelines(final)
        file.write("\n")
        print (final)
    file.close()
generator(mayus)
