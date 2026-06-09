budega = (
    'Arroz', 19.99,
    'Feijão', 12.99,
    'Óleo', 9.99,
    'Papel Higiênico', 21.99,
    'Temperos', 3.49,
    'Refrigerante', 11.99
)

print(f'{'':-<18}Budega do Zé{'':-<18}')

for c in range(0, len(budega), 2):
    # print(budega[c], '-------', budega[c+1]) - O de baixo faz exatamente isso, porém organizando os espaçamentos.
    produto = budega[c]
    preco = budega[c+1]
    print(f'Produto:{produto:-<30}  R${preco}')