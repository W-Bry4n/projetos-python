# Calculadora de Frete
def cabecalho():
    print("\n" + "=" * 30)
    print('SISTEMA DE LOGISTICA')
def calculo_frete(peso):
    if peso <= 20:
        return peso * 10.00
    else:
        return peso * 15.00
cabecalho()
peso = float(input("Digite o peso da carga em (kg):"))
frete = calculo_frete(peso) 
print(f"O valor do frete é: R$ {frete: .2f}")
print("=" * 30)