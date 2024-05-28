print ("******Bienvenido a Burger King******")
print ("Ingrese los datos para la factura electrónica")
nombre = input("Ingrese su nombre: ")
cedula = input("Ingrese su número de cédula: ")
mail = input("Ingrese su correo electrónico: ")
number_Hamburgesa = int (input ("Ingrese el número de hamburgesas que desea: "))

print ("Ingrese el tipo de hamburgesa que desea ordenar (1/2/3): ")
print ("1) Sencilla ")
print ("2) Doble ")
print ("3) Triple ")
tipo_Hamburgesa = int(input (" "))

print ("Ingrese el tipo de pago que va a realizar (1/2): ")
print ("1) Tarjeta de crédito ")
print ("2) Efectivo ")
tipode_Pago = int(input (" "))

total = 0

if tipo_Hamburgesa == 1 and tipode_Pago == 1 :
    total = (1.50*number_Hamburgesa) + (1.50*0.05) 
elif tipo_Hamburgesa == 1 and tipode_Pago == 2 :
    total = (1.50*number_Hamburgesa)
elif tipo_Hamburgesa == 2 and tipode_Pago == 1 :
    total = (2.50*number_Hamburgesa) + (2.50*0.05)
elif tipo_Hamburgesa == 2 and tipo_Hamburgesa == 2 :
    total = (2.50*number_Hamburgesa)
elif tipo_Hamburgesa == 3 and tipode_Pago == 1 :
    total = (3.25*number_Hamburgesa) + (3.25*0.05)
elif tipo_Hamburgesa == 3 and tipode_Pago == 2 :
    total = (3.25*number_Hamburgesa)
else :
        total = None
        print("No existe este tipo de hamburgesa o el tipo de pago")    

if total is not None:
    print ("FACTURA ELECTRÓNICA")
    print(f"Nombre: {nombre}")
    print(f"Cédula: {cedula}")
    print(f"Correo electrónico: {mail}")
    print(f"Número de hamburguesas: {number_Hamburgesa}")
    print(f"Total a pagar: ${total:.2f}")

