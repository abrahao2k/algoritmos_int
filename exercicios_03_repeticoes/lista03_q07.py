'''7) Escreva um programa que pergunta o
valor inicial de uma dívida, a taxa
mensal de juros e o valor que será pago
a cada mês. Informe o número de meses
necessários para quitar a dívida, o
total pago e quanto de juros foi pago.'''

divida = float(input("Dívida: "))
divida_inicial = divida
juros  = float(input("Taxa de Juros: "))
parcela = float(input("Parcela mensal: "))
meses = 0
total_pago = 0
while divida > 0:
    meses = meses + 1
    if divida >= parcela:
        divida = divida - parcela
        total_pago += parcela
        juros_mes = divida * juros/100
        divida = divida + juros_mes
    else:
        total_pago += divida
        divida = 0
    
print("Meses = ", meses)
print(f"Total pago = R$ {total_pago:.2f}")
print(f"Juros pagos = R$ {total_pago - divida_inicial:.2f}")