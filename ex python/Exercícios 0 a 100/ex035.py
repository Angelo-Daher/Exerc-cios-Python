c1 = float(input("Digite a primeira metragem: "))
c2 = float(input("Digite a segunda metragem: "))
c3 = float(input("Digite a terceira metragem: "))

if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('Podemos formar um triangulo!')
else:
    print('Não podemos formar um triangulo!')
