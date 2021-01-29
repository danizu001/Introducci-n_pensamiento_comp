objetivo = int(input('Escoge un numero: '))
epsilon = 0.01
paso = epsilon**2 
respuesta = 0.0

while respuesta**2 < objetivo and respuesta <= objetivo:
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada {objetivo}')
else:
    print(f'La raiz cudrada de {objetivo} es {respuesta}')