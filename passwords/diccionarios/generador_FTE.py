#Creador : https://www.facebook.com/TheNinjaBlack2
#PRogramado en python3 - sudo apt-get install python3 python3-dev 
#Si usas windows ve ha la web de python :  https://www.python.org/  y descargate el instalador 
#version exacta : 3.4,pero lo he chekado en backtrack con python 3.1 y corre nice
#cualquier duda mensaje ha mi perfil de fb 
#El generador,genera un millon de posibles contrasenas
#si se que el codigo debe mejorar xd
from random import choice
import os
import sys
if sys.platform.startswith == 'linux':
    limpiar = "clear"
else :
    limpiar = "cls"
os.system(limpiar)
print  ("""
Modo de uso : 
Open Terminal>python3 generador_FTE.py
Creador : python3 generador_FTE.py creador
informacion : python3 generador_FTE.py informacion""")
if 'creador' in sys.argv:
   print ("creador: https://www.facebook.com/TheNinjaBlack2")
   exit(0)
elif 'informacion' in sys.argv:
    print ("""Hasta donde se este tipo de redes suelen ser de la A hasta la Z y numeros,todo en minuscula,siendo ovbio no incluir   nada 
	raro por el estilo,ire actualizando el generador mientras consiga mas infomacion nueva sobre este tipo de redes""")
    exit(1)
def algo():
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    file = open('generador.txt','w')
    print ("Se esta creando el diccionario,espera ha que termine o cancelalo 'control + c'")
    for i in range(1000000):
       final = ''.join([choice (caracteres) for i in range(10)])
       generar = file.writelines(final)
       file.write("\n")
    cerrar = file.close()
    print ("Ya ha terminado de crearse el diccionario")
algo()