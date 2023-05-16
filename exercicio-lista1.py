'''
Solicite 10 números inteiros ao usuário e armazene os números pares em uma lista, 
e os números ímpares em outralista.Exibaas duas listas ao usuário.

'''
pares = []
impares = []

for n in range(10):
    numero = int(input('Número: '))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(pares)
print(impares)
