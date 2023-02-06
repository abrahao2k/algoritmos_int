'''2. Crie um programa em que o usuário
digite 10 valores em uma lista e
depois imprima a lista.'''

lista = []   #lista vazia
cont = 1
while cont <= 10:
    info = input("Digite a informação: ")
    lista.append(info)
    cont += 1
    
print(lista)