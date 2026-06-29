numeros = []

while True:
    n = int(input('Digite um número: '))
    numeros.append(n)

    continuar = str(input('Deseja Continuar?[S/N] '))
    if continuar in 'Ss':
        continue
    
    else:
        break

print(f'Temos {len(numeros)} números!')
print(f'Foram digitados os números: {numeros}')
numeros.sort(reverse = True)
print(f'Os números em ordem decrescente são: {numeros}')
if 5 in numeros:
    print('O número 5 está na lista!')
else:
    print('Não há nenhum número 5 na lista!')