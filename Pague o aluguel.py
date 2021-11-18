valor_divida = int(input())
valor_mensal = int(input())
pagamento = 0
while valor_divida > 0:
    pagamento = pagamento + 1
    print('pagamento:', pagamento)
    print('antes =', valor_divida)
    valor_divida = valor_divida - valor_mensal
    if valor_divida < 0:
        print('depois =',0)
        print('-----')
    else:
        print('depois =', valor_divida)
        print('-----')
