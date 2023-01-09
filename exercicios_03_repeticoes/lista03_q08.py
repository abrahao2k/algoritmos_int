'''
8) Escreva um programa que apresente a série de Fibonacci até o décimo quinto termo. A série de
Fibonacci é formada pela sequência: 1, 1, 2, 3, 5, 8, 13, 21, 34, ..., etc. Esta série se caracteriza pela
soma de um termo atual com o seu anterior subsequente, para que seja formado o próximo valor
da sequência. Portanto começando com os números 1, 1 o próximo termo é 1+1=2, o próximo é
1+2=3, o próximo é 2+3=5, o próximo 3+5=8, etc.'''

anterior = 0
atual = 1

contador = 1

while contador <= 15:
    
    print(atual)
    proximo = anterior + atual
    anterior = atual
    atual = proximo

    contador += 1
