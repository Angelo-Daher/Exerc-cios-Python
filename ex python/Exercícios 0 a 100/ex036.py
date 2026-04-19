import math
casa = float(input("Digite o valor da casa: "))
salario = float(input('Qual o valor do seu salário: '))
limite = salario * 30 / 100
parcelas = casa / limite
parcelas = math.ceil(parcelas)

print('Para a compra ser aprovada, o valor das parcelas não pode exceder 30% do seu salário')
print(f'Neste caso, seria razoável a partir de {parcelas} parcelas.')

parcelas = int(input('Quantos parcelas? '))
pm = casa / parcelas

if pm <= limite:
    print('Compra Aprovada!')
    print(f'Voce pagará parcelas de {pm:.3f} reais em {parcelas} meses.')
else:
    print('Compra Reprovada!')
