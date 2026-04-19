from datetime import date
ano = int(input("Digite o ano de nascimento: "))
categoria = date.today().year - ano

if categoria <= 9:
    print('Vc é um atleta MIRIM')
elif categoria > 9 and categoria <= 14:
    print('Vc é um atleta INFANTIL')
elif categoria > 14 and categoria <= 19:
    print('Vc é atleta JUNIOR')
elif categoria > 19 and categoria <= 25:
    print('Vc é um atleta SENIOR')
elif categoria > 25:
    print('Vc é um atleta MASTER')
else:
    print('Inválido!')
