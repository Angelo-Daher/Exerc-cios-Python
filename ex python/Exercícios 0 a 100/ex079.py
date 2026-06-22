valores = []

while True:
    n = int(input('Digite um número: '))
    if n not in valores:
        valores.append(n)
    
    elif n in valores:
        print('Este número já foi adicionado!')

    resposta = str(input('Deseja continuar? '))
    while resposta != 'sim' or resposta != 'nao':
        print('Digite apenas sim ou nao!')
        resposta = str(input('Deseja continuar? '))

    if resposta in 'sim' or resposta in 's':
        continue

    elif resposta in 'nao' or resposta in 'n':
        break

    else:
        while resposta != 'sim' or resposta != 'nao':
            print('Digite apenas sim ou nao!')
            resposta = str(input('Deseja continuar? '))

valores.sort()
print(f'Os valores escolhidos de forma organizada são: {valores}')
