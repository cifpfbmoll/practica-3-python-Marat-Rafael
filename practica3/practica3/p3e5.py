# Marat-Rafael

#ejercicio 5
"""Pida un número que como máximo tenga tres cifras 
(por ejemplo serían válidos 1, 99 i 213 pero no 1001). Si el usuario introduce
un número de más de tres cifras debe un informar con un mensaje de error como
este “ERROR: El número 1005 tiene más de tres cifras”."""

num=int(input("introduce por favor un numero con tres cifras como maximo: "))

error = "ERROR: El número '{0}' tiene más de tres cifras"

if (-1000<num<1000):
    
    print ("Has indicado numero ",num)
    
else:
    
    print (error.format(num))
    
    