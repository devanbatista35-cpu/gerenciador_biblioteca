# Arquivo principal do programa, onde conecta os outros arquivos

from utils import titulo
from livros import (
    cadastrar_livro, listar_livros, atualizar_status,
    ver_historico_concluidos, filtrar_por_genero,
    contar_por_status, deletar_livro, buscar_livro
)

def mostrar_menu():
    titulo("🏛️ Devan's Library 📚")
    print("1. Cadastrar Livro")
    print("2. Listar Livros")
    print("3. Buscar Livro")
    print("4. Atualizar Status")
    print("5. Contar por Status")
    print("6. Filtrar por Gênero")
    print("7. Histórico de Concluídos")
    print("8. Deletar Livro")
    print("9. Sair\n")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_livro()
    elif opcao == "2":
        listar_livros()
    elif opcao == "3":
        buscar_livro()
    elif opcao == "4":
        atualizar_status()
    elif opcao == "5":
        contar_por_status()
    elif opcao == "6":
        filtrar_por_genero()
    elif opcao == "7":
        ver_historico_concluidos()
    elif opcao == "8":
        deletar_livro()
    elif opcao == "9":
        print("Encerrando o programa...👋\n")
        break
    else:
        print("Opção inválida. Tente novamente.\n")
