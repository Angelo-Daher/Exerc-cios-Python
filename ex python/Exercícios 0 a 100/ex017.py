cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
oposto = cateto_oposto ** 2
adjacente = cateto_adjacente ** 2
hipotenusa = oposto + adjacente 
hipo = hipotenusa ** (1/2)
print(f'O comprimento da Hipotenusa é {hipo:.2f}')
