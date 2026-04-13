km = float(input('Quantos km o carro percorreu? '))
dias = int(input('Quantos dias alugado? '))
dia = dias * 60
rodado = km * 0.15
print(f'O carro percorreu {km} km, alugado por {dias} dias!')
print(f'O preço a pagar é {dia + rodado}!')
