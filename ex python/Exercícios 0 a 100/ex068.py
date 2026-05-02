import random

print("""-=-=-=-=-=-=-=-=-=-=-=-=-
VAMOS JOGAR PAR OU ÍMPAR 
-=-=-=-=-=-=-=-=-=-=-=-=-""")

s = 0

while True:
    usuario = int(input('Digite um valor: '))
    escolha = str(input('Par ou Ímpar [P/I]: ')).upper()
    computador = random.randint(1, 1000)
    soma = usuario + computador

    if escolha == 'P':
        if soma % 2 == 0:
            s += 1
            print(f"""Você jogou {usuario} e o computador jogou {computador}. Total de {soma}. DEU PAR.""")
            print('Vamos jogar denovo?')

        else:
            print(f'GAME OVER! DEU ÍMPAR. Vc venceu {s} vezes.')
            break

    elif escolha == 'I':
        if soma % 2 == 1:
            s += 1
            print(f"""Você jogou {usuario} e o computador jogou {computador}. Total de {soma}. DEU ÍMPAR.""")
            print('Vamos jogar denovo?')

        else:
            print(f'GAME OVER! DEU PAR. Vc venceu {s} vezes.')
            break

    else:
        print('Escolha inválida. Digite P ou I.')
    
  