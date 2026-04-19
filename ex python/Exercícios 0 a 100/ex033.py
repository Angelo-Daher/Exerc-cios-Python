n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
n3 = int(input('Terceiro numero: '))

maior = n1
if n2 > n1:
    maior = n2
elif n3 > n1:
    maior = n3
print(f'O maior número é: {maior}')

menor = n1
if n1 > n2:
    menor = n2
elif n1 > n3:
    menor = n3
print(f'O menor número é: {menor}')
