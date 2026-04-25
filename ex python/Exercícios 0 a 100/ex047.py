import time
contador = 0
for num in range(0, 51, 1):
    if num % 2 == 0:
        contador += 1
        print(num)
        time.sleep(1)
print(f'Neste intervalo de tempo, temos {contador} números pares!')