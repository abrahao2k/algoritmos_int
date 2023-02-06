'''6. Crie um programa que sorteie números
aleatórios entre 1 e 100. Preencha uma lista
com 20 elementos *diferentes*, organize em
ordem decrescente e imprima na tela.
'''

import random
numeros = []
x = 1
while x <= 20 :
    sorteado = random.randint(1,100)
    if sorteado in numeros:
        continue   #se já existe, sorteia denovo
    else:
        numeros.append(sorteado)
        x += 1

numeros.sort(reverse=True) #ordena decrescente
print(numeros)