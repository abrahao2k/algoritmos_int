'''5. Crie um programa que o usuário digita
os dados de duas listas com 3 elementos cada. 
Depois crie uma terceira lista com a junção
dos elementos das outras duas. Imprima a nova 
lista'''

lista1 = []
lista1.append(input("Digite: "))
lista1.append(input("Digite: "))
lista1.append(input("Digite: "))

lista2 = []
lista2.append(input("Digite:"))
lista2.append(input("Digite:"))
lista2.append(input("Digite:"))

lista3 = lista1 + lista2
print(lista3)
