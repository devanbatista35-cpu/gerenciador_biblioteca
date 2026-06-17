#Arquivo que recebe as configurações

from dados import livros, fila_a_ler, pilha_concluidos, prioridades, status, contador_id
from utils import titulo, validar_inteiro
from validacoes import validar_texto, validar_ano

# 1- Cadastrar Livro
def cadastrar_livro():
    global contador_id
    titulo("Cadastrar Livro")
    
    titulo_livro = validar_texto("Título: ", "Título")
    autor = validar_texto("Autor: ", "Autor")
    ano = validar_ano("Ano: ")
    genero = validar_texto("Gênero: ", "Gênero")

    print(" - Prioridades: 1. Baixa | 2. Média | 3. Alta")
    opcao = input("Prioridade: ")

    if opcao == "1":
        prioridade = prioridades[0]
    elif opcao == "2":
        prioridade = prioridades[1]
    else:
        prioridade = prioridades[2]

    contador_id += 1

    dict_livro = {
        "id": contador_id,
        "titulo": titulo_livro,
        "autor": autor,
        "ano": ano,
        "genero": genero,
        "prioridade": prioridade,
        "status": status[0]
    }

    livros.append(dict_livro)
    fila_a_ler.append(dict_livro)
    print("Livro cadastrado com sucesso!✅\n")

# 2- Listar Livros
def listar_livros():
    titulo("Listar Livros")
    if len(livros) == 0:
        print("❌ Nenhum livro cadastrado.\n")
        return

    for i, livro in enumerate(livros, start=1):
        print(f"LIVRO: {i}")
        print(f"ID: {livro['id']}")
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano: {livro['ano']}")
        print(f"Gênero: {livro['genero']}")
        print(f"Prioridade: {livro['prioridade']}")
        print(f"Status: {livro['status']}\n")

# 3- Buscar Livro
def buscar_livro():
    titulo("Buscar Livro")

    if len(livros) == 0:
        print("❌ Nenhum livro cadastrado. A busca não foi realizada.\n")
        return

    termo = validar_texto("Digite parte do título ou autor: ", "Busca").lower()

    encontrados = [
        livro for livro in livros
        if termo in livro["titulo"].lower() or termo in livro["autor"].lower() ]

    if len(encontrados) == 0:
        print("❌ Nenhum livro encontrado com esse termo.\n")
        return

    for i, livro in enumerate(encontrados, start=1):
        print(f"LIVRO: {i}")
        print(f"ID: {livro['id']}")
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano: {livro['ano']}")
        print(f"Gênero: {livro['genero']}")
        print(f"Prioridade: {livro['prioridade']}")
        print(f"Status: {livro['status']}\n")

# 4- Atualizar Status
def atualizar_status():
    titulo("Atualizar Status")
    listar_livros()

    if len(livros) == 0:
        return

    id_livro = validar_inteiro(input("Digite o ID do livro: "), "Digite um número válido.")
    if id_livro is None:
        return

    for livro in livros:
        if livro["id"] == id_livro:
            print("\nEscolha o novo status:")
            print("1 - A Ler")
            print("2 - Lendo")
            print("3 - Concluído")
            
            opcao = input("Opção: ")

            if opcao == "1":
                livro["status"] = status[0]
                if livro not in fila_a_ler:
                    fila_a_ler.append(livro)
            elif opcao == "2":
                livro["status"] = status[1]
            elif opcao == "3":
                livro["status"] = status[2]
                if livro not in pilha_concluidos:
                    pilha_concluidos.append(livro)
                if livro in fila_a_ler:
                    fila_a_ler.remove(livro)

            print("Status atualizado com sucesso!✅\n")
            return
    print("❌ Livro não encontrado.\n")


# 5- Contar por Status
def contar_por_status():
    titulo("Contagem de Livros por Status")
    total_a_ler = sum(1 for livro in livros if livro["status"] == status[0])
    total_lendo = sum(1 for livro in livros if livro["status"] == status[1])
    total_concluido = sum(1 for livro in livros if livro["status"] == status[2])

    print(f"A Ler: {total_a_ler}")
    print(f"Lendo: {total_lendo}")
    print(f"Concluídos: {total_concluido}")
    print(f"Total geral: {len(livros)}\n")

# 6- Filtrar por Gênero
def filtrar_por_genero():
    titulo("Filtrar por Gênero")
    genero = validar_texto("Digite o gênero: ", "Gênero")
    encontrados = [livro for livro in livros if livro["genero"].lower() == genero.lower()]

    if len(encontrados) == 0:
        print("❌ Nenhum livro encontrado para esse gênero.\n")
        return

    for i, livro in enumerate(encontrados, start=1):
        print(f"LIVRO: {i}")
        print(f"ID: {livro['id']}")
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano: {livro['ano']}")
        print(f"Gênero: {livro['genero']}")
        print(f"Prioridade: {livro['prioridade']}")
        print(f"Status: {livro['status']}\n")

# 7- Ver Histórico de Concluídos
def ver_historico_concluidos():
    titulo("Histórico de Livros Concluídos")
    if len(pilha_concluidos) == 0:
        print("❌ Nenhum livro concluído.\n")
        return

    for i, livro in enumerate(reversed(pilha_concluidos), start=1):
        print(f"LIVRO CONCLUÍDO: {i}")
        print(f"ID: {livro['id']}")
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano: {livro['ano']}")
        print(f"Gênero: {livro['genero']}")
        print(f"Prioridade: {livro['prioridade']}\n")

# 8- Deletar Livro
def deletar_livro():
    titulo("Deletar Livro")
    listar_livros()

    if len(livros) == 0:
        return

    id_livro = validar_inteiro(input("Digite o ID do livro a deletar: "), "Digite um número válido.")
    if id_livro is None:
        return

    for livro in livros:
        if livro["id"] == id_livro:
            livros.remove(livro)
            if livro in fila_a_ler:
                fila_a_ler.remove(livro)
            if livro in pilha_concluidos:
                pilha_concluidos.remove(livro)
            print("Livro deletado com sucesso!✅\n")
            return
    print("❌ Livro não encontrado.\n")

