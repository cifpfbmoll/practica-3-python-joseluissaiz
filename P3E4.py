# Practica 3
#   Ejercicio4
#       Pide al usuario que introduzca 3 calificaciones, y calcule la media
#       de estas.
#
#
#inputs
calificacion1 = input("Introduce la primera cualificacion :")
calificacion2 = input("Introduce la segunda cualificacion :")
calificacion3 = input("Introduce la tercera cualificacion :")
#
#Operacion
try:
    resultado = (float(calificacion1) + float(calificacion2) + 
    float(calificacion3))/3
    print ("La media es de " + str(resultado))
except TypeError:
    print ("Los valores no son validos")