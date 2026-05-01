print('=== PROGRESSÃO ARITMÉTICA ===')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

termo = primeiro
contador = 1
total = 0
mais = 10  # começa mostrando 10 termos

while mais != 0:
    total += mais
    
    while contador <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        contador += 1
    
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? (0 para parar): '))

print(f'Progressão finalizada com {total} termos mostrados.')