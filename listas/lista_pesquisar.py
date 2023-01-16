herois = ['homem-aranha','superman',
         'batman','wolverine','chapolim']

nome = input("Qual herói você procura? ")
if nome in herois:
    print(nome, "vai salvar você!")
    print("Posição:", herois.index(nome))
else:
    print("Esse não pode lhe ajudar.")