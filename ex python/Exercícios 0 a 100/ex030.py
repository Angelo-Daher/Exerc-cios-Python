vel = int(input("Qual a velocidade do carro? "))
multa = (vel - 80)
valor = multa * 7
if vel > 80:
    print(f'Voce ultrapassou {multa} km e sua multa ficou em torno de {valor} reais')
elif vel < 80 and vel > 60:
    print('Voce está quase no limite da velocidade!')
elif vel > 40 and vel < 60:
    print('Permaneça nesta velocidade!')
else:
    print('Velocidade permitida')
