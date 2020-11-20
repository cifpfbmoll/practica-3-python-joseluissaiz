# Practica 3
#   Ejercicio5
#       Pida un numero que como maximo tenga tres cifras (por ejemplo serian
#        validos 1, 99 i 213, pero no 1001). Si el usuario introduce un numero
#        de mas de tres cifras debe un informar con un mensaje de error como
#        este "ERROR: El numero 1005 tiene mas de tres cifras".
#
#
#
#input
num = input("Introduce un numero de tres cifras o menos :")
#
#Contando cifras . . .
numCount = len(num)
#Operacion
#
if numCount <= 3:
    print("El numero " + str(num) + " contiene " + str(numCount) + " cifras")
else:
    print("ERROR: El numero " + str(num) + 
    " supera el limite de cifras (" + str(numCount) + ")")