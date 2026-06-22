valores = []

while True:
    n = int(input('Digite um número: '))
    if n not in valores:
        valores.append(n)
    
    elif n in valores:
        print('Este número já foi adicionado!')

    resposta = str(input('Deseja continuar? '))
    while resposta not in ['sim', 'nao', 's', 'n']:
        print('Digite apenas sim ou nao!')
        resposta = str(input('Deseja continuar? '))

    if resposta in ['sim', 's']:
        continue

    elif resposta in ['nao', 'n']:
        break


valores.sort()
print(f'Os valores escolhidos de forma organizada são: {valores}')
