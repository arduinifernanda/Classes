preco = float(input())

quantidade = int(input())

if quantidade <= 40:
    
    total = preco * quantidade
    desconto1 = 0.10 + (quantidade * 0.01)
    total_desconto = total - (total * desconto1)
    print (f' {total:.2f}')
    print(f' {total_desconto:.2f}')
