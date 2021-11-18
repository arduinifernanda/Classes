inicio = int(input())
fim = int(input())
primos = 0
if (0 <= inicio <= fim <= 5000):
    while inicio <= fim:
        divisor = 0
        for num in range(1, inicio + 1):
            if inicio % num == 0:
                divisor += 1
        if divisor <= 2:
            print(inicio)
            primos += 1
        inicio += 1
print('primos:', primos)
