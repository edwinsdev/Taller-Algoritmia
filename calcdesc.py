# El algoritmo debe calcular el precio con descuento basado en una condición.
# debe llevar entrada de datos, condicionales, operadores aritméticos 

pre = float(input("Ingrese el precio original del descuento: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))
condicion = int(input("Ingrese la cantidad de unidades a comprar: "))
if condicion >= 10:
    precio_final = pre - (pre * (descuento / 100))
elif condicion >=2 and condicion < 10:
    precio_final = pre
    print("El precio final es: ", precio_final)  # El precio final es:
else:
    print("No se aplica el descuento")  # No se aplica el descuento
