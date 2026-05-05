numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

num = int(input('Digite apenas de 1 a 20: '))
while num < 1 or num > 20:
    num = int(input('Tente Novamente! Digite apenas de 1 a 20: '))
print(f'Voce escolheu o número {numeros[num]}')
