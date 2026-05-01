n = int(input('Digite um valor: '))

contador = 1
somador = n
maior = n
menor = n

opcao = str(input('Deseja digitar mais algum valor [S/N]: ')).upper()
while opcao not in 'SN':
      print('Digite apenas S ou N!')
      opcao = str(input('Deseja digitar mais algum valor [S/N]: ')).upper()

while opcao != 'N':
    n = int(input('Digite outro valor: '))

    contador += 1
    somador += n

    if n > maior:
        maior = n
    if n < menor:
        menor = n

    opcao = str(input('Deseja digitar mais algum valor [S/N]: ')).upper()
    while opcao not in 'SN':
        print('Digite apenas S ou N!')
        opcao = str(input('Deseja digitar mais algum valor [S/N]: ')).upper()
    
media = (somador / contador)

print(f'Programa encerrado! A média entre os valores é de {media:.2f}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
    