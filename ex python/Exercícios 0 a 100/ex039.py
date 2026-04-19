from datetime import date
ano = int(input('Em que ano vc nasceu: '))
idade = date.today().year - ano

if idade == 18:
    print('É hora de vc fazer o alistamento militar!')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos para vc se alistar!')
elif idade > 18:
    print(f'Já passou {idade - 18} anos do tempo de seu alistamento!')
