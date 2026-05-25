# Simulador de investimento CDB #
deposito = float(input("digite o valor do aporte "))
meses = int(input("quantos meses vai investir? "))
taxa = 0.0116
conversao = taxa/100
total = 0

for mes in range (1, meses +1):
    total = total + deposito
    total = total + (total * taxa)
    print(f"Ao final do Mês {mes}, você terá: R${total:2f}") 



Nome: Willian Bryan de Oliveira
