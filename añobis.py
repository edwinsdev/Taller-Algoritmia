# Determinar si un año es bisiesto

anno = int(input("Ingrese a continuacion el año el cual desea verificar: "))
if anno % 4 == 0 and (anno % 100 != 0 or anno % 400 == 0):
    print(f"El año {anno} es bisiesto")
else:
    print(f"El año {anno} no es bisiesto")