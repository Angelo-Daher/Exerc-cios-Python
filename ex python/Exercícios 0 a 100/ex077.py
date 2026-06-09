words = (
    'Cama', 'Parede', 'Computador', 'Microfone', 'Gamer', 'Som',
    'Fio', 'Mouse', 'Cadeira', 'Salao', 'Ventilador', 'Aparador'
)

for item in words:
    vogais = ''
    for letra in item:
        if letra in 'aeiou':
            vogais += letra
    print(f'Na palavra {item}, temos as vogais {vogais}!')