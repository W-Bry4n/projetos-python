# Simulador de investimento de poupança #
deposito = float(input("digite o valor do Aporte "))
taxa = float(input("Qual a taxa da poupança "))
meses = int(input("Quantos meses vai investir "))
conversao = taxa/100
total = 0

for mes in range (1, meses +1):
    total = total + deposito
    total = (total * taxa) + total 
print(f"Ao final do período, você terá: R${total:2f}")