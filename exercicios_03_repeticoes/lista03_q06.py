'''6) Escreva um programa que pergunta o valor de depósito
inicial para uma poupança, e a taxa de rendimento mensal.
Apresente o saldo dos próximos 24 meses, considerando o
rendimento sobre o saldo atual de cada mês.
'''
# saldo = saldo + (saldo * rendimento/100)

saldo = float(input("Quanto é o depósito inicial? "))
rendimento = float(input("Quanto é a taxa de rendimento? "))
mes = 1
while mes <= 24:
    saldo = saldo + (saldo * rendimento / 100)
    print(f"Mês {mes} = R$ {saldo:.2f}")
    mes = mes + 1

