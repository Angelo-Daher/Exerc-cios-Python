sal = float(input("Qual o seu salario? "))
if sal > 1250.00:
    print(f'Seu salário teve ajuste de 10% e o novo valor é de {sal + (sal * 10 / 100)}')
else:
    print(f'Seu salário teve ajuste de 15% e o novo valor é de {sal + (sal * 15 / 100)}')
