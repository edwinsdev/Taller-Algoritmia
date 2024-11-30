num1 = float(input("Ingrese a continuacion el primer numero: "))
num2 = float(input("Ingrese a continuacion el segundo numero; "))
num3 = float(input("Ingrese a continuacion el tercer numero: "))

print(" ")
print("Espere, ahora mismo estamos validando su solicitud")
print("...")
print("...")
print("...")
print("...")
print(" ")

if num1 > num2 and num1 > num3:
    print(f"El numero mayor ingresado es: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"El mayor numero ingresado es: {num2}")
elif num3 > num2 and num3 > num1:
    print(f"El mayor numero ingresado es: {num3}")
else:
    print(f"Los numeros que ingresaste han sido todos iguales, se reinicia el programa")