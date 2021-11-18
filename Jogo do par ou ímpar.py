numero = int(input())

if numero >= 2:
    if numero % 2 == 0:
        n_par1 = numero + 2
        n_impar1 = numero -1
        print(n_impar1, n_par1)
    else:
        n_par2 = numero + 1
        n_impar2 = numero - 2
        print(n_impar2, n_par2)
