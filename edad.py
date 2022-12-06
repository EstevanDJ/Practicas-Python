nombre = input("Como te llamas")
edad = int(input("Escriba su edad"))
if edad < 25:
    print("Eres un Estudiante")
elif edad > 65:
    print("Eres un Master")
elif edad > 25:
    print("Eres un Profesor")
