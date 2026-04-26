frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

if junto == inverso:
    print('A frase é um palíndromo!')
else:
    print('A frase NÃO é um palíndromo!')