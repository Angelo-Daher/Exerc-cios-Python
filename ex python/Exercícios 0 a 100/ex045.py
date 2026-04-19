import random

itens = ('Pedra', 'Papel', 'Tesoura')

computador = random.randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))

print('-=' * 15)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 15)

if computador == jogador:
    print('EMPATE!')
elif computador == 0:  # computador jogou pedra
    if jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:  # computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:  # computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
