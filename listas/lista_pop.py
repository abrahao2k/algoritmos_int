lista = ['RN','CE','PE','PB','BA','RJ']
#         0     1    2    3   4     5
lista.pop(2)
print(lista)
lista.pop(2)
print(lista)
lista.pop(0)
print(lista)

posicao = int(input("Apagar qual posição? "))
if posicao < len(lista):
    lista.pop(posicao)
    print(lista)
else:
    print("Posição não existe.")