''' 11) Elaborar um programa que efetue a
leitura de valores positivos inteiros até
que um valor negativo seja informado.
Ao final devem ser apresentados o maior e
o menor valores informados pelo usuário.'''
cont=0
while True:
    num = int(input("Digite um número: "))
    cont += 1
    if num < 0 :
        break
    else:
        if cont==1:
            maior = num
            menor = num
        else:
            if num < menor:
                  menor = num
            
            if num > maior:
                  maior = num

print(f"Maior: {maior}")
print(f"Menor: {menor}")

