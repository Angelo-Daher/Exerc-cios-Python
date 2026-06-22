livros = []

while True:
    livro = str(input('Digite o nome do livro: '))
    while livro in livros:
        print('Este livro já está cadastrado!')
        livro = str(input('Digite o nome do livro: '))
        
    else:
        livros.append(livro)

    continuar = (input('Deseja continuar? '))
    if continuar.lower() != 's':
        break
    
print(livros)

