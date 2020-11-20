# Practica 3
#   Ejercicio2
#       Pida al usuario el espacio recorrido por un coche y el tiempo que ha
#       tardado en horas y que calcule a que velocidad media habia realizado
#       el recorrido.
#
#inputs
espacioRecorrido = input("¿Cuantos kilometros ha recorrido el coche? :")
tiempoRecorrido = input("¿Cuantas horas a tardado? :")
#
#Operacion
try:
    resultadoRecorrido = float(espacioRecorrido)/float(tiempoRecorrido)
    print("El coche circulaba a " + str(resultadoRecorrido) + "km/h")
except TypeError:
    print("Valores incorrectos")