produtos = ['café','bolo','pão','queijo']
print(produtos)
produtos.remove('bolo')
print(produtos)
nome = input("Excluir qual? ")
if nome in produtos:
    produtos.remove(nome)
    print(produtos)
else:
    print(nome,"não existe na lista.")