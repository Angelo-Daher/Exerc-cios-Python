valores = []
for contagem in range(0 , 5):
    valores.append(int(input('Digite um valor: ')))

for indice, valor in enumerate(valores):
    print(f"Na posição {indice} temos o valor {valor}")

print(f'O maior valor digitado foi {max(valores)} na posição {valores.index(max(valores))}!')
print(f'O menor valor digitado foi {min(valores)} na posiçaõ {valores.index(min(valores))}!')