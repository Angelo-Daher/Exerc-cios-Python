valores = []
for contagem in range(0 , 5):
    valores.append(int(input('Digite um valor: ')))


maior = max(valores)
menor = min(valores)


print(valores)
print(f'O maior valor digitado foi {maior} nas posições ',end='')


for indice, valor in enumerate(valores):

    if valor == maior:
        print(indice,end='... ')


print(f'O menor valor digitado foi {menor} nas posições ',end=' ')

for indice, valor in enumerate(valores):

    if valor == menor:
        print(indice,end='... ')
        


#print(f'O maior valor digitado foi {max(valores)} nas posições {len(valores.index(max(valores)))}!') - SERVEM PORÉM, só pegam a primeira ocorrencia 
#print(f'O menor valor digitado foi {min(valores)} nas posições {valores.index(min(valores))}!')