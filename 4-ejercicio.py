print("Seleccione una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. Salir")
opcion = input("Ingrese una opción (1-4): ")

if opcion == "1":
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    print(f"Resultado de la suma: {a + b}")
if opcion == "2":
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    print(f"Resultado de la resta: {a - b}")
if opcion == "3":
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    print(f"Resultado de la multiplicación: {a * b}")
if opcion == "4":
    print("¡Hasta luego!")
if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
    print("Opción inválida. Intente de nuevo.")




