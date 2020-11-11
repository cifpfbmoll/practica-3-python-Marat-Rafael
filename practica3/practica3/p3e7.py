# Marat-Rafael


#ejercicio 7
"""Pida al usuario tres número que serán el día, mes y ano. 
Comprueba que la fecha introducida es válida.  Por ejemplo: 
32/01/2017->Fecha incorrecta
29/02/2017->Fecha incorrecta
30/09/2017->Fecha correcta.
"""

print("Para comprobar si fecha es valida, introduce dia mes y ano: ")

dia=int(input("introduce el dia: "))

mes=int(input("introduce el mes: "))

ano=int(input("inptoduce el ano: "))

if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12) and 0<dia<=31:
    
    print (dia,mes,ano,"correcto")
    
elif (mes==4 or mes==6 or mes==9 or mes==11) and 0<dia<=30 :
    
    print (dia,mes,ano,"correcto2")
    
elif mes==2:
    
    if ano%4==0 and 0<dia<=29:
        
        print (dia, mes, ano,"correcto3")
        
    elif ano%4!=0 and 0<dia<=28:
        
        print (dia,mes,ano,"correcto4")
        
    else:
        
        print (dia,mes,ano,"Error1")
else:
    
    print (dia,mes,ano,"Error2")
