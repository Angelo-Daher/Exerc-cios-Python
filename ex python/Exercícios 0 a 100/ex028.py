import random
computador = random.randint(0, 5)
usuario = int(input("Digite um numero entre 0 e 5: "))
if usuario == computador:
    print('Voce acertou')
else:
    print('Voce errou, quer tentar denovo? ')
