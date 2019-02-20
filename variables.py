# crie uma função que receba uma lista de 20 valores aleatórios, retornar apenas o maior valor e printar em tela. 
# crie uma lista com 10 números aleatórios. itere essa lista e printar em tela os valores que são ímpares e pares.

import random 

lista = []
i=1

while i <=20:
    lista.append(random.randrange(1,200))
    i = 1 + i


print (f'Essa lista foi gerada aleatoriamente: {lista}')

def maximo_valor(lista):
    return max (lista, key=int)

print (f'Meu maior valor é: {maximo_valor(lista)}')









