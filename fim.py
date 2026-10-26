import csv
from pathlib import Path


ARQUIVO = Path(__file__).with_name("dados.csv")

empresa = {
    "nome": "EletroMax",
    "localização": "São Paulo",
    "início": "23 de março de 2012",
}

recursos = [
    "Teclado Logitech",
    "Monitor Samsung",
    "Mouse Logitech",
    "Headset HyperX",
    "Mousepad Logitech",
]


def carregar_estoque():
    estoque = []
    with open(ARQUIVO, "r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor, None)  # Pula o cabeçalho.
        for linha in leitor:
            codigo, nome, custo, quantidade = linha
            codigo_numero = int(codigo)
            if not 1 <= codigo_numero <= 99:
                raise ValueError(f"O código {codigo} não é válido.")
            codigo = f"{codigo_numero:02d}"
            if any(item[0] == codigo for item in estoque):
                raise ValueError(f"O código {codigo} aparece mais de uma vez no CSV.")
            estoque.append([codigo, nome, float(custo), int(quantidade)])
    return estoque


def salvar_estoque(estoque):
    with open(ARQUIVO, "w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["codigo_id", "nome", "custo", "quantidade"])
        escritor.writerows(estoque)


def mostrar_empresa():
    print("\nDados da empresa:")
    for chave, valor in empresa.items():
        print(f"{chave.capitalize()}: {valor}")
    print("Recursos em operação:")
    for recurso in recursos:
        print(f"- {recurso}")


def mostrar_csv():
    print("\nConteúdo do arquivo dados.csv:")
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        cabecalho = arquivo.readline()
        print(cabecalho, end="")
        linha = arquivo.readline()
        while linha:
            print(linha, end="")
            linha = arquivo.readline()


def pedir_numero(mensagem, minimo=0):
    while True:
        entrada = input(mensagem).strip()
        try:
            numero = int(entrada)
            if numero >= minimo:
                return numero
            print(f"Erro: digite um número igual ou maior que {minimo}.")
        except ValueError:
            print("Erro: digite um número inteiro válido.")


def pedir_id():
    while True:
        entrada = input("Digite o código ID do produto (01 a 99): ").strip()
        try:
            codigo = int(entrada)
            if 1 <= codigo <= 99:
                return f"{codigo:02d}"
            print("Erro: o ID deve estar entre 01 e 99.")
        except ValueError:
            print("Erro: digite um ID numérico válido.")


def procurar_produto(estoque, codigo):
    for produto in estoque:
        if produto[0] == codigo:
            return produto
    return None


def exibir_estoque(estoque):
    print("\nID | Produto | Custo | Quantidade")
    print("-" * 42)
    for codigo, nome, custo, quantidade in estoque:
        print(f"{codigo} | {nome} | R$ {custo:.2f} | {quantidade}")
        if quantidade < 5:
            print("  Estoque baixo!")


def atualizar_quantidade(estoque):
    produto = procurar_produto(estoque, pedir_id())
    if produto is None:
        print("Erro: produto não encontrado.")
        return
    produto[3] = pedir_numero("Digite a nova quantidade: ")
    salvar_estoque(estoque)
    print("Quantidade atualizada.")


def registrar_venda(estoque):
    produto = procurar_produto(estoque, pedir_id())
    if produto is None:
        print("Erro: produto não encontrado.")
        return
    quantidade = pedir_numero("Quantas unidades foram vendidas? ", 1)
    if quantidade > produto[3]:
        print("Erro: não há estoque suficiente.")
        return
    produto[3] -= quantidade
    salvar_estoque(estoque)
    print("Venda registrada.")


def cadastrar_produto(estoque):
    codigo = pedir_id()
    if procurar_produto(estoque, codigo) is not None:
        print("Erro: esse ID já está cadastrado.")
        return

    nome = input("Digite o nome do produto: ").strip()
    while not nome:
        print("Erro: o nome não pode ficar vazio.")
        nome = input("Digite o nome do produto: ").strip()

    while True:
        try:
            custo = float(
                input("Digite o custo do produto: R$ ").strip().replace(",", ".")
            )
            if custo >= 0:
                break
            print("Erro: o custo não pode ser negativo.")
        except ValueError:
            print("Erro: digite um custo válido.")

    quantidade = pedir_numero("Digite a quantidade em estoque: ")
    estoque.append([codigo, nome, custo, quantidade])
    salvar_estoque(estoque)
    print("Produto cadastrado.")


def excluir_produto(estoque):
    produto = procurar_produto(estoque, pedir_id())
    if produto is None:
        print("Erro: produto não encontrado.")
        return
    estoque.remove(produto)
    salvar_estoque(estoque)
    print("Produto excluído.")


def menu():
    mostrar_empresa()
    mostrar_csv()
    try:
        estoque = carregar_estoque()
    except (OSError, ValueError, csv.Error) as erro:
        print(f"Erro ao carregar o estoque: {erro}")
        return

    while True:
        print(
            "\n1 - Exibir estoque"
            "\n2 - Atualizar quantidade"
            "\n3 - Registrar venda"
            "\n4 - Cadastrar produto"
            "\n5 - Excluir produto"
            "\n6 - Sair"
        )
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            exibir_estoque(estoque)
        elif opcao == "2":
            atualizar_quantidade(estoque)
        elif opcao == "3":
            registrar_venda(estoque)
        elif opcao == "4":
            cadastrar_produto(estoque)
        elif opcao == "5":
            excluir_produto(estoque)
        elif opcao == "6":
            print("Sistema encerrado.")
            break
        else:
            print("Erro: opção inválida.")


if __name__ == "__main__":
    menu()