i = 1
soma = 0
while i <= 3:
    nota = float(input('Digite uma nota entre 0 e 10:'))
    while (nota < 0 or nota > 10):
        nota = float(input('***Digite uma nota entre 0 e 10:'))
    soma = soma + nota
    i = i + 1
print('A soma das notas é:', soma)
