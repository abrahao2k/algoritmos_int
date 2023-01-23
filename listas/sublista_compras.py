compras = []
while True:
    nome = input("Nome do produto: ")
    preco = float(input("Preco do produto: "))
    compras.append([nome,preco])
    mais = input("Mais itens? (s/n) ")
    if mais == 'n':
        break
print(compras)
print(len(compras), "itens na lista.")

## PARA SABER O VALOR TOTAL DAS COMPRAS ##
total = 0
x = 0
while x < len(compras):    #PERCORRER A LISTA
    total += compras[x][1]
    x += 1
print("Total = R$", total)