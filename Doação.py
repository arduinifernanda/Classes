valor = float(input())
vc = 0
while valor != -1.00:
    vc = vc + valor
    valor = float(input())
print(f'VC$ {vc:.2f}')
    
reais = vc * 2.50
print(f'R$ {reais:.2f}')
