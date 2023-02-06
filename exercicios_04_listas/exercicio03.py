''' 3. Crie um programa que sorteie 10 números
entre 1 e 100 e guarde-os numa lista. Ordene
a lista em ordem crescente e imprima na tela
os valores sorteados.'''

import random
numeros = []
x = 1
while x <= 10 :
  numeros.append(random.randint(1,100))
  x = x + 1
numeros.sort()
print(numeros)



