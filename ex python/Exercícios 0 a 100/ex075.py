valores = []
pares = []

for c in range(0, 7):
    value = int(input(f'Digite o valor {c+1}: '))
    while value not in range(0, 100):
        print('Digite somente números entre 0 e 100!')
    if value % 2 == 0:
        pares.append(value)

    valores.append(value)

valores_tupla = tuple(valores)
valores_pares = tuple(pares)

print('Os valores escolhidos foram:', valores_tupla)
print(f'O valor 9 apareceu {valores_tupla.count(9)} vezes!')
if 3 not in valores_tupla:
    print('O valor 3 não foi digitado em nenhuma posição!')
else:
    print('O primeiro valor 3 foi digitado na posição', valores_tupla.index(3))

if valores_pares:
    print('Os números pares escolhidos são:', valores_pares)
else:
    print('Não foram escolhidos valores pares!')
