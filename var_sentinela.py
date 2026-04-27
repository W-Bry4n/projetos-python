# - Exemplo de uso da variável sentinela
while True:
 comando = input("Digite um comando para parar. Digite 'sair' ")
 if comando == "sair":
  break
print(f"Executado: {comando}")