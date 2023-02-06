'''4. Crie um programa que cadastre os alunos
de uma escola. Pergunte ao usuário o nome,
o curso e a série de um aluno. Salve esses 3
dados como uma (sub)lista e depois acrescente
esta (sub)lista em uma lista principal.
O programa deve repetir quantas vezes o
usuário desejar. Ao finalizar os cadastros,
imprima todos os alunos cadastrados.
'''

escola = []
repetir = "sim"
while repetir == "sim":
    nome  = input("Digite o nome do aluno: ")
    curso = input("Digite o curso do aluno: ")
    serie = input("Digite a série do aluno: ")
    aluno = [nome, curso, serie]
    escola.append(aluno)
    repetir = input("Cadastrar outro? (sim/nao) ")

print(escola)
