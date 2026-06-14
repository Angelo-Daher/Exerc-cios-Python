valores = []

n = int(input('Digite um valor: '))
valores.append(n)

num = str(input('Deseja digitar mais valores? '))
while num == 'SIM' or num == 'sim':
    int(input('Digite um valor: '))
    str(input('Deseja digitar mais valores? '))
    valores.append(num)

print(valores)