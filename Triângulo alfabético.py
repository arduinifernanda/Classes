n = int(input())
if n >= 1 and n <= 26:  
    vezes = 1
    letra = 'A'
    while vezes <= n:
        print(letra * vezes)
        vezes += 1
        letra = chr(ord(letra) + 1)
