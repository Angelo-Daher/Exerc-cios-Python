contador = 0
somador = 0

for c in range(1, 7):
    num = int(input('Escolha um número: '))
    if num % 2 == 0:
        contador += 1
        somador += num
print(f'Ao final, foram escolhidos {contador} números pares, e a soma de todos os pares é de {somador}')