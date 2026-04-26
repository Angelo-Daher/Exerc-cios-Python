pesos = []
for c in range(1, 6):
    peso = float(input('Digite o peso: '))
    pesos.append(peso)
print(f'O maior peso é {max(pesos)}')
print(f'O menor peso é {min(pesos)}')