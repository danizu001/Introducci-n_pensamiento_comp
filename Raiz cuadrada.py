objetivo = int(input("Escoge un entero: "))
respuesta = 0

while respuesta**2<objetivo:
    respuesta += 1
    
if respuesta**2 == objetivo:
        print("La raíz es: " + str(respuesta))
else: 
        print("La raíz no es exacta")