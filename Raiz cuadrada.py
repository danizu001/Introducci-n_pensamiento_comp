def sqrtBinario(objetivo, epsilon=0.01):
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2
    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
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
sqrtBinario(objetivo)
sqrtAprox(objetivo)
sqrtBasico(objetivo)