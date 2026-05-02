n = s = 0
qn = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    qn += 1
    s += n 

print('Acabou!')
print(f'Foram digitados {qn} números e a soma entre eles é de {s}.')