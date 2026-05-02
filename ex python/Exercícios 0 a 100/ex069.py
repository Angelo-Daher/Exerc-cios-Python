maiores18 = 0
homens = 0
mulheres = 0

print('--------------------')
print('Cadastre uma pessoa!')
print('--------------------')

while True:

    idade = int(input('Digite a idade: '))
    

    sexo = str(input('Digite o sexo [M/F]: ')).upper()
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).upper()

    if idade > 18:
        maiores18 += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F':
        if idade < 20:
            mulheres += 1

    question = str(input('Quer continuar [S/N]? ')).upper()
    while question not in 'SN':
        question = str(input('Quer continuar [S/N]? ')).upper()
    if question == 'N':
        break

print('Programa encerrado!')
print(
    f'{maiores18} pessoas são maiores de 18 anos, foram cadastrados {homens} homens e {mulheres} mulheres tem menos de 20 anos!')
