import os
import random

# Nome do arquivo onde os dados serão armazenados
ARQUIVO_CODIGOS = "codigos_detalhados.txt"

def gerar_codigo_unico_aleatorio():
    # Carrega os códigos já gerados
    codigos_gerados = set()
    if os.path.exists(ARQUIVO_CODIGOS):
        with open(ARQUIVO_CODIGOS, "r") as arquivo:
            for linha in arquivo:
                codigo, _, _ = linha.split(";", maxsplit=2)
                codigos_gerados.add(codigo)

    # Verifica se ainda há códigos disponíveis
    total_possibilidades = 16**4
    if len(codigos_gerados) >= total_possibilidades:
        raise ValueError("Todos os códigos possíveis já foram gerados!")

    # Gera códigos aleatórios até encontrar um único
    while True:
        numero = random.randint(0, total_possibilidades - 1)  # Aleatório entre 0 e 65535
        codigo = f"{numero:04X}"  # Formata como hexadecimal de 4 dígitos
        if codigo not in codigos_gerados:
            return codigo

def salvar_codigo(codigo, nome, descricao):
    # Salva o código, nome e descrição no arquivo
    with open(ARQUIVO_CODIGOS, "a") as arquivo:
        arquivo.write(f"{codigo};{nome};{descricao}\n")

def pesquisar_codigo(codigo):
    # Pesquisa um código no arquivo
    if os.path.exists(ARQUIVO_CODIGOS):
        with open(ARQUIVO_CODIGOS, "r") as arquivo:
            for linha in arquivo:
                codigo_salvo, nome, descricao = linha.strip().split(";", maxsplit=2)
                if codigo_salvo == codigo:
                    return nome, descricao
    return None, None

def main():
    # Gera um novo código
    try:
        codigo = gerar_codigo_unico_aleatorio()
        print(f"Código gerado: {codigo}")
        
        # Solicita informações adicionais
        nome = input("Insira um nome (opcional): ").strip()
        descricao = input("Insira uma descrição (obrigatória): ").strip()
        
        if not descricao:
            print("A descrição é obrigatória. Tente novamente.")
            return
        
        # Salva as informações
        salvar_codigo(codigo, nome if nome else "N/A", descricao)
        print("Código salvo com sucesso!")
    except ValueError as e:
        print(e)

def pesquisar():
    codigo = input("Digite o código a ser pesquisado: ").strip().upper()
    nome, descricao = pesquisar_codigo(codigo)
    if descricao:
        print(f"Código: {codigo}")
        print(f"Nome: {nome}")
        print(f"Descrição: {descricao}")
    else:
        print("Código não encontrado.")

if __name__ == "__main__":
    try:
        print("1. Gerar novo código")
        print("2. Pesquisar código")
        opcao = input("Escolha uma opção: ").strip()

        # Se o usuário pressionar Enter, define como "1"
        if not opcao:
            opcao = "1"

        if opcao == "1":
            main()
        elif opcao == "2":
            pesquisar()
        else:
            print("Opção inválida.")

    except KeyboardInterrupt:
        print("\nProcesso interrompido pelo usuário.")