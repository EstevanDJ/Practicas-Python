nombre = input("Como te llamas")
edad = input("Cuantos años tienes")
while not edad.isdigit():
    edad = input("Digita un numero")
edad = int(edad)
if edad < 25:
    print("Eres Estudiante")
elif edad >= 65:
    print("Eres Master")
elif edad > 25:
    print("Eres Profesor")
