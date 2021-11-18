ano = int(input())
fim = int(input())
contagem = 0

while ano <= fim:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(ano)
        contagem = contagem + 1
    ano = ano + 1
    
print('bissextos:', contagem)
