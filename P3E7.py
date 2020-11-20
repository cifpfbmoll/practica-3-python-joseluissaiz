# Practica 3
#   Ejercicio 7
#       Pida al usuario tres número que serán el día, mes y año. Comprueba que 
#       la fecha introducida es válida.
#
#----------------inputs
dia = input("Introduce el dia :")
mes = input("Introduce el mes :")
anyo = input("Introduce el año :")
#
#
#----------------Variables
#error counting
countError = 0
bisiesto = False
#
#---------------Logic
#comprobante de tamaño
if int(dia) > 31 or int(dia) <= 0 or int(mes) <= 0 or int(mes) > 12 or \
(int(mes) == 2 and int(dia) > 29):
    countError += 1
#
#comprobante de meses que tienen 31 dias
if (int(dia) > 31 and int(mes) == 4) or (int(dia) > 31 and int(mes) == 6) or \
(int(dia) > 31 and int(mes) == 9) or (int(dia) > 31 and int(mes) == 11):
    countError += 1
#
#comprobante de años bisiestos
if int(anyo) % 4 == 0:
    if int(anyo) % 100 == 0:
        if int(anyo) % 400 == 0:
            bisiesto = True
        else:
            bisiesto = False
    else:
        bisiesto = True
else:
    bisiesto = False
#
#
if bisiesto == True and int(mes) == 2 and int(dia) > 28:
    countError += 1
#
#
#
#--------------Resultado
if countError == 0:
    print ("La fecha es correcta")
else:
    print("La fecha NO es correcta")