#Aluno1: Formato do Nome do Filme
def formatar (nome):
    return nome.upper()
#Aluno2: Verificação de acesso
def verificador (idade):
    if idade>=18:
        return "Autorizado"
    else:
        return "Não autorizado" 
#Aluno3: Mensagem de Retorno
def gerar_mensagem (status):
 if status == "autorizado":
  return "Tenha uma ótima sessão"
 else:
  return "Sinto muito, idade não autorizada"
#Aluno4: Integrador do Projeto
nome_filme = input("Digite o nome do filme ")
idade_filme = int(input("Digite sua idade "))
filme = formatar(nome_filme)
status_final = verificador(idade_filme)
mensagem = gerar_mensagem(status_final)
print(f"\n Filme:{filme}")
print(f"status:{status_final}")
print(f"aviso:{mensagem}")
