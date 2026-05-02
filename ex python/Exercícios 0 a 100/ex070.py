total = 0
produtos1000 = 0
maisbarato = ''
menorpreço = 0
contador = 0

print('------ Mercadinho da Drikosa ------')

while True:
    nome = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o valor do produto: '))

    contador += 1
    if contador == 1:
        maisbarato = nome
        menorpreço = preço
    elif preço < menorpreço:
        maisbarato = nome
        menorpreço = preço

    if preço > 1000:
        produtos1000 += 1

    total += preço
    ask = str(input('Deseja continuar? ')).upper()
    if ask == 'N':
        break

print(f'Foram gastos R${total} com a compra. {produtos1000} produtos foram mais de 1000,00 reais e o produto mais barato foi a/o {maisbarato} que custou R${menorpreço} reais.')