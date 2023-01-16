alunos = []
repet = "s"
while repet == "s":
    nome = input("Digite o aluno: ")
    alunos.append(nome)
    repet = input("Repetir?(s/n) ")

print(alunos)
print(len(alunos), "alunos na lista.")