def invertido(texto):
    return texto[::-1]
palavra = 'programação'
palavra_invertida = invertido(palavra)
print(palavra_invertida)
print(palavra == palavra_invertida)