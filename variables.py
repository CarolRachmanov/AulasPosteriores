# crie uma função que receba uma lista de 20 valores aleatórios, retornar apenas o maior valor e printar em tela. 
# crie uma lista com 10 números aleatórios. itere essa lista e printar em tela os valores que são ímpares e pares.


# 1
# import random 

# lista = []
# i=1

# while i <=20:
#     lista.append(random.randrange(1,2000))
#     i = 1 + i


# print (f'Essa lista foi gerada aleatoriamente: {lista}')

# def maximo_valor(lista):
#     return max (lista, key=int)

# print (f'Meu maior valor é: {maximo_valor(lista)}')

#2

import random 

lista = []
i = 1 

while i <=10:
     lista.append(random.randrange(1,200))
     i=1+i

print (f'Essa é minha lista: {lista}')    


for i in lista:
    if i%2 == 0:
        # lista_pares= [i,i+1]
        # print(lista_pares)
        print(f'{i} é par')
    else:
        print(f'{i} é ímpar')


# Deu certo, mas eu queria que a resposta saísse numa nova lista de pares e uma nova lista de ímpares 








