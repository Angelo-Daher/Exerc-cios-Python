n = int(input('Digite um número: '))
if n <= 1:
    eh_primo = False
else:
    for c in range(2, n):
        if n % c == 0:
            eh_primo = False
            break  # para o loop assim que achar um divisor

if eh_primo:
    print('Este número é um número primo!')
else:
    print('Este não é um número primo!')