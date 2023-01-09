#aluno = ["Alberto", "Informática", 3]
#print(f"{aluno[0]} cursa o {aluno[2]}° ano de {aluno[1]}.")

nome = input("Qual o nome do aluno? ")
curso = input("Qual o curso do aluno? ")
serie = input("Qual a série do aluno? ")
aluno = [nome, curso, serie]
print(f"{aluno[0]} cursa o {aluno[2]}° ano de {aluno[1]}.")

aluno[0] = "Fernanda Silva"  # atualizar uma posição
print(f"{aluno[0]} cursa o {aluno[2]}° ano de {aluno[1]}.")

