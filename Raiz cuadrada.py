import time
def sqrtBinario(objetivo, epsilon=0.01):
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2
    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) / 2
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def sqrtAprox(objetivo, epsilon=0.01):
    paso=epsilon**2
    respuesta=0
    while respuesta**2 < objetivo and respuesta <= objetivo:
        respuesta += paso    
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'La raiz cudrada de {objetivo} es {respuesta}')

def sqrtBasico(objetivo):
    respuesta=0
    while respuesta**2<objetivo:
        respuesta += 1
        
    if respuesta**2 == objetivo:
            print("La raíz es: " + str(respuesta))
    else: 
            print("La raíz no es exacta")

objetivo = int(input('Escoge un numero: '))

op=int(input("Digite que opción quiere: 1.Bin 2.Aprox 3.Básico "))

if op==1:
    comienzo=time.time()
    sqrtBinario(objetivo)
    final=time.time()
    print(final-comienzo)
elif op==2:
    comienzo=time.time()
    sqrtAprox(objetivo)
    final=time.time()
    print(final-comienzo)
elif op==3:
    comienzo=time.time()
    sqrtBasico(objetivo)
    final=time.time()
    print(final-comienzo)
else:
    print("Opción incorrecta")