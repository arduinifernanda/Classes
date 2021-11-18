soma = 0
#repeticao definida
for i in range(1,4):
    nota = float(input('Digite uma nota entre 0 e 10:'))
#repeticao indefinida
    while (nota < 0 or nota > 10):
        nota = float(input('***Digite uma nota entre 0 e 10:'))
    soma = soma + nota
    i = i + 1
print('A soma das notas é:', soma)
