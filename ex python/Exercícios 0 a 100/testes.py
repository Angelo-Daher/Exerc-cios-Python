n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break 
    s += n
print('Acabou!')
print(f'A soma dos números é de {s}')