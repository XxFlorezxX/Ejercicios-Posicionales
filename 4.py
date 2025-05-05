edad = int(input("Ingrese edad: "))
licencia = input("Ingrese licencia (si/no): ").lower()  
if edad >= 18 and licencia == "si":
    print("Puede conducir")
else:
    print("No puede conducir")