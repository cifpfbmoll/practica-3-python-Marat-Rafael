# Marat-Rafael

#Pide al usuario que introduzca 3 calificaciones, y calcule la media de estas.

print ("Vamos a calcular una media de tres notas")

nota1=float(input("introduce por favor la primera nota: "))

nota2=float(input("introduce por favor la segunda nota: "))

nota3=float(input("introduce por favor la tercera nota: "))

media=(nota1+nota2+nota3)/3

print ("la nota media de '{0}', '{1}' y '{2}' es '{3:.1f}' ".format(nota1,nota2,nota3,media))