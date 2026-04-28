n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

opcao = 0 # Initialize opcao
while opcao != 5:
  print("""Escolha uma opção:
[1] Somar
[2] Multiplicar 
[3] Maior 
[4] Novos Números
[5] Sair do Programa""")
  opcao = int(input('Escolha uma opção: '))

  if opcao == 1:
    print(f'A soma dos dois números é',{n1 + n2})

  elif opcao == 2:
    print(f'A multiplicação dos dois números é' {n1 * n2})

  elif opcao == 3:
    maior = n1 
    if n2 > n1:
      maior = n2
      print(f'O maior número é o {maior}')

  elif opcao == 4 :
    print('Informe os novos números!')
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))

print('Programa encerrado!')
