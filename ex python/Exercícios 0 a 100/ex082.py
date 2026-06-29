numeros = []
pares = []
impares = []

while True:
    n = int(input('Digite um número: '))
    numeros.append(n)

    if n %2 == 0:
        pares.append(n)

    elif n %2 == 1:
        impares.append(n)

    continuar = str(input('Deseja Continuar?[S/N] '))
    if continuar in 'Ss':
        continue
    
    else:
        break

print(f'Temos um total de {len(numeros)} números digitados!')
print(f'Na lista principal temos os números: {numeros}')
print(f'Os números pares digitados foram: {pares}')
print(f'Os números ímpares digitados foram: {impares}')