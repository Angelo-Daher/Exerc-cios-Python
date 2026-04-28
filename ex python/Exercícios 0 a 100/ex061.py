primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

print('Os 10 primeiros termos da PA são:')

contador = 0
termo_atual = primeiro_termo
while contador < 10:
    print(termo_atual, end=' ')
    termo_atual += razao
    contador += 1
print()
