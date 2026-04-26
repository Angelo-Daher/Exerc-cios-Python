soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''
mulheres_menos_20 = 0

for c in range(1, 5):
    print(f'---- {c}ª pessoa ----')
    
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    
    soma_idade += idade

    if sexo == 'M':
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_homem_mais_velho = nome

    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

media_idade = soma_idade / 4

print(f'\nA média de idade do grupo é {media_idade}')
print(f'O homem mais velho é {nome_homem_mais_velho}')
print(f'Ao todo são {mulheres_menos_20} mulheres com menos de 20 anos')