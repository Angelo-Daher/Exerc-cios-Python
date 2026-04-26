from datetime import date
maior = 0
menor = 0
atual = date.today().year
for c in range(1, 8):
    p = int(input('Digite a ano de nascimento: '))
    idade = atual - p
    if idade >= 18:
        maior += 1
    elif idade < 18:
        menor += 1
print(f'No total, {maior} pessoas são maiores de idade e {menor} são menores de idade!')
    
