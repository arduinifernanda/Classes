nota_trabalho = float(input())
nota_prova = float(input())
if nota_trabalho >= 0 and nota_trabalho <= 10 and nota_prova >= 0 and nota_prova <= 10:
    if (nota_trabalho + nota_prova) / 2 >= 6:
        print("aprovado")
    else:
        if nota_trabalho >=2:
            print("talvez com a sub")
        else:
            print("reprovado")
