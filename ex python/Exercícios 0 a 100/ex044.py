print('========= Mercadinho ==========')
produto = float(input('Digite o valor do produto: '))
print(""" Escolha a forma de pagamento:
[1] á vista dinheiro/cheque: 10% de desconto
[2] á vista no cartão: 5% de desconto
[3] em até 3x no cartão: preço normal
[4] 3x ou mais no cartão: 20% de juros""")

opcao = int(input('Digite uma opção: '))
if opcao == 1:
    print(f'O valor a ser pago será de {produto - (produto * 10 / 100)}')
elif opcao == 2:
    print(f'O valor a ser pago será de {produto - (produto * 5 / 100):.2f}')
elif opcao == 3:
    print(f'O valor a ser pago continuará sendo {produto}, pois na opção escolhida não há descontos!')
elif opcao == 4:
    print(f'O valor a ser pago será de {produto + (produto * 20 / 100)}')
else:
    print('Opção invalida!')
