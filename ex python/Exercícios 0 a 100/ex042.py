c1 = float(input("Digite a primeira metragem: "))
c2 = float(input("Digite a segunda metragem: "))
c3 = float(input("Digite a terceira metragem: "))

if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('Podemos formar um triangulo!')
    if c1 == c2 and c2 == c3 and c3 == c1:
        print('E será um triangulo EQUILÁTERO')
    elif c1 == c2 or c2 == c3 or c3 == c1:
        print('E será um triangulo ISÓCELES')
    elif c1 != c2 and c2 != c3 and c3 != c1:
        print('E será um triangulo ESCALENO')
else:
    print('Não podemos formar um triangulo!')
