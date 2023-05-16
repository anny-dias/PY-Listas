# Fazer uma função que realize a busca por um número em uma lista

def busca(lista, item):
    for n in lista:             #percorre os itens da lista
        if n == item:           #verifica se o valor é o que está sendo buscado
            return True
    return False                #se não encontrar o valor retorna False 

# preencher uma lista
lista = []
while True:
    n = int(input('Informe im número inteiro (0 para finalizar): '))
    if n == 0:
        break
    lista.append(n)
print(lista)

item = int(input('Informe um número para buscar na lista: '))
if busca(lista, item):      #chama a função
    print('O número está contido na lista')
else: 
    print(f'O número {item} não está contido na lista')
    