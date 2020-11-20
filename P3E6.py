# Practica 3
#   Ejercicio6
#       Pida al usuario el precio de un producto y el nombre del producto 
#       con el precio del IVA (21%). Por ejemplo: "Tu bicicleta vale 100 
#       euros y con el 21% de IVA se queda en 121 euros en total".
#
#input
productoNombre = input("Nombre del producto? :")
productoPrecio = input("Cuanto cuesta el producto (€) :")
#
#Operacion
#
try:
    productoPrecioIva = float(productoPrecio) + (float(productoPrecio)/21)*100
    productoPrecioIva = round(productoPrecioIva, 2)
    print("Tu " + productoNombre + " con el 21 por ciento de IVA se queda en " +
    "un total de " + str(productoPrecioIva) + "€.")
except TypeError:
    print("El valor introducido no es correcto")