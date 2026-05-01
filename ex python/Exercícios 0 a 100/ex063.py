print('=== SEQUÊNCIA DE FIBONACCI ===')

n = int(input('Quantos termos você quer mostrar? '))

a = 0
b = 1

for i in range(n):
    print(f'{a} -> ', end='')
    proximo = a + b
    a = b
    b = proximo

print('FIM')