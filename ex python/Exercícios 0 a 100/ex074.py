from random import randint #Chama a biblioteca Random 
n_aleatorios = [] #Lista para guardar os numeros escolhidos no loop abaixo

for n in range(0, 5): #Loop com for para escolher a quantidade de numeros e serem escolhidos
    n = randint(0, 20) #A função randint sorteia e escolhe os numeros de 0 a 20 
    n_aleatorios.append(n) #A função append adiciona os numeros escolhidos na lista criada anteriormente (n_aleatorios)

numeros_escolhidos = tuple(n_aleatorios) #A função tuple transforma a lista (n_aleatorios) e uma tupla através de uma nova variável

print('Os números escolhidos foram:',numeros_escolhidos) #mostra os numeros escolhidos e armazenados na tupla
print('O maior número escolhido foi:',max(numeros_escolhidos)) #A função max mostra o maior número escolhido
print('O menor número escolhido foi:', min(numeros_escolhidos)) #A funçao min mostra o menor numero escolhido