# Ferramenta de conversão dólar x real
def converter(valor_dolar):
    taxa = 5.15
    valor_real = valor_dolar * taxa
    return valor_real
print("conversor Dolár x Real")
preco = float(input("Digite o preço do produto em Dólar:"))
resultado = converter(preco)
print(f"O valor em reais é: {resultado:2f}"))
