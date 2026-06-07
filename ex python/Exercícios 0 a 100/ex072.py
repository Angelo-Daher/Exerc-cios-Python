numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

num = int(input('Digite apenas de 0 a 20: '))
while num not in range(0,21):
    num = int(input('Tente novamente. Digite apenas de 0 a 20: '))
print(f'Voce escolheu o número {numeros[num]}')
