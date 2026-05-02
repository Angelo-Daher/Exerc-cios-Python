print('======== Programa TABUADA ========')

n = int(input('Quer ver a tabuada de qual valor? '))

while n > 0:
    print('===========================')
    for c in range(1, 11):
        print(n,'x',c, '=', (n*c))

    print('---------------------------')
    n = int(input('Quer ver a tabuada de qual valor? '))

print('===========================')
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')
print('===========================')