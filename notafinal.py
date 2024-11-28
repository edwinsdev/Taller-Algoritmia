notamin = float(input("Ingrese la nota minima necesaria para aprobar la materia: "))
notatuya = float(input("Ingrese la nota que saco el estudiante y la cual desea comprobar: "))

if notatuya < notamin:
    print ("El estudiante reprobo la materia")
else:
    print ("El Estudiante aprobo la materia")
