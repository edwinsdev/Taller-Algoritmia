name = str(input("Ingrese aca su nombre: "))
user = str(input("Ingrese aca su nombre de usuario como (edwinsdev): "))
password = str(input("Ahora ingrese su contraseña. "))
conpass = str(input("Confirme su contraseña: "))

if conpass == password:
    print(f"Perfecto, {name} Ahora puedes acceder a nuestra pagina")
else:
    print("Su contraseña es incorrecta")
