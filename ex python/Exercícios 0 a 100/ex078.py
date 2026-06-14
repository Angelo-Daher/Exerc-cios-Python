valores = []
for contagem in range(0 , 5):
    valores.append(int(input('Digite um valor: ')))

for indice, o_que_tem_no_indice_tal in enumerate(valores):
    print(f"Na posição {indice} temos o valor {o_que_tem_no_indice_tal}")

print(f'O maior valor digitado foi {max(valores)} e o menor valor digitado foi {min(valores)}!')