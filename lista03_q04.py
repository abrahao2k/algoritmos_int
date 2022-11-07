''' 4) Digite as notas de uma prova para uma turma
de 10 alunos e calcule a média da turma.
Dica: use uma variável para acumular a soma de
todas as notas, por último, já fora do laço,
faça a divisão para calcular a média.
'''
soma = 0
contador = 1                  # var. controle
while contador <= 10:         # teste lógico
    nota = float(input(f"Digite a nota do aluno {contador}: "))
    soma = soma + nota
    contador = contador + 1   # incremento
else:
    media = soma / 10
    print(f"A média da turma é: {media:.1f}")