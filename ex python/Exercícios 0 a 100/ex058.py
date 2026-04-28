import random

contador = 0
computador = random.randint(0, 10)
jogador = int(input('Escolha um número entre 0 e 10: '))

while jogador != computador:
    if jogador > 10:
        print('Número inválido, escolha somente de 0 a 10!')
    elif jogador < computador:
        print('Mais um pouco!')
    elif jogador > computador:
        print('Menos um pouco!')
   
    jogador = int(input('Escolha um número entre 0 e 10: '))
    contador += 1

print('Você acertou, parabéns!')
