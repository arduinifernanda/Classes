inicio = int(input())
fim = int(input())
quantidade_primos = 0

def eh_primo(valor):
    if valor < 2:
        return False
    elif valor == 2:
        return True
    else:
        for i in range(2, valor):
            if valor % i == 0:
                return False
        print(valor)
        return True
if (inicio <= fim <= 5000):
    for i in range(inicio, fim + 1):
        if eh_primo(i):
            quantidade_primos += 1
print(f'primos: {quantidade_primos}')
