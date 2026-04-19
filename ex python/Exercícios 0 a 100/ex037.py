num = int(input('Digite um número inteiro: '))
print("""Escolha uma das bases para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL""")
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(bin(num)[2:])
elif opcao == 2:
    print(oct(num)[2:])
elif opcao == 3:
    print(hex(num)[2:])
else:
    print('Opção invalida! Escolha Novamente!')
