# Calculadora De Propinas

#Nombre 
#Precio
#Total

nombre = input("Ingrese su nombre:")

try:
    precio = float(input("Ingrese el valor de la comida:"))

    if  precio < 20:
        porcentaje = 0.10

    elif precio >= 20 and precio <=50:
        porcentaje = 0.15

    else:
        porcentaje = 0.20

    propina = precio * porcentaje 
    total = precio + propina

    print("Hola", nombre)
    print("La propina es: $", propina)
    print("El total a pagar es: $", total)

except ValueError:
    print("Error: Debes ingresar un numero valido para el precio")

