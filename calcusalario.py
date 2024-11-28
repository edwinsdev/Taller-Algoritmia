salario = int(input("Ingrese Su Salario: "))
desc = 0.19
descximp = salario*desc

print (f"El descuento que le sera realizado del salario es del {desc * 100} %")
print (f"El salario neto que usted recibe mensualmente es: {salario - descximp}")