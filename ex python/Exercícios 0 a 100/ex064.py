contador = 0
somador = 0

n = int(input('Digite um número: '))
while n != 999:
    contador += 1
    somador += n
    n = int(input('Digite um número: '))

print('Programa Encerrado!')
print(f'Foram digitados {contador} números e a soma entre eles é de {somador}!')