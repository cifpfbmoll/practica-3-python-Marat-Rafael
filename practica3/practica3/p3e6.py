# Marat-Rafael

#ejercicio6
"""Pida al usuario el precio de un producto y el nombre del producto y muestre 
el mensaje con el precio del IVA (21%). Por ejemplo: 
“Tu bicicleta vale 100 euros y con el 21 % de IVA se queda en 121 euros en total”."""

print ("Vamos a calcular precio del producto con la IVA 21%")

producto=input("introduce por favor el nombre del producto: ")

precio=int(input("indica por favor el precio del producto: "))

iva=precio*0.21

print ("Tu",producto," vale ",precio," euros y con el 21 % de IVA se queda en",precio+iva," euros en total")

