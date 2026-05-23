📚 Sistema de Gerenciamento de Biblioteca

📖 Visão Geral
Este projeto é um **sistema de gerenciamento de biblioteca em console**, desenvolvido em Python. Ele permite cadastrar livros, atualizar status de leitura, filtrar por gênero, buscar e manter um histórico de livros concluídos.  

⚙️ Funcionalidades
- Cadastrar livro com título, autor, ano, gênero e prioridade.  
- Listar livros com detalhes.
- Buscar livros. 
- Atualizar status (A Ler, Lendo, Concluído).  
- Contar por status. 
- Filtrar por gênero.  
- Ver histórico de livros concluídos (pilha). 
- Deletar livro.  

🧩 Exemplo: FIFO, LIFO, Listas, Dicionário e Tuplas

Comportamento FIFO: Primeiro livro cadastrado é o primeiro a ser lido

primeiro_a_ler = fila_a_ler[0]

Comportamento LIFO: Último livro concluído é exibido primeiro

ultimo_concluido = pilha_concluidos[-1]

Comportamento Dicionário: Estrutura de dados mutável que armazena informações   

    dict_livro = {
        "id": contador_id,
        "titulo": titulo_livro,
        "autor": autor,
        "ano": ano,
        "genero": genero,
        "prioridade": prioridade,
        "status": status[0]
    }

Comportamento Lista: Uma coleção ordenada e mutável de elementos que permite duplicatas e manipulação dinâmica de itens.

livros = []   lista global de livros que armazena os objetos

Comportamento Tupla: Uma coleção ordenada e imutável, cujos valores não podem ser alterados ou modificados após a sua criação.

prioridades = ("Baixa", "Média", "Alta")  # tupla de prioridades valores imutaveis
status = ("A Ler", "Lendo", "Concluído")  # tupla de status valores imutaveis

  
🚀 Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/library-system.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd library-system
   ```
3. Execute o programa:
   ```bash
   python main.py
   ```

📋 Requisitos
- Python 3.8+  
- Nenhuma biblioteca externa necessária (implementação pura em Python).  

🛠️ Uso
Ao iniciar, o programa exibe um menu com opções:
- `1` → Cadastrar livro  
- `2` → Listar Livros  
- `3` → Buscar Livros  
- `4` → Atualizar Status  
- `5` → Contar por Status  
- `6` → Filtrar por Gênero 
- `7` → Histórico de Concluídos  
- `8` → Deletar  
- `9` → Sair  

🤝 Contribuição
Contribuições são bem-vindas!  
- Faça um fork do repositório  
- Crie uma nova branch  
- Commit suas alterações  
- Abra um Pull Request  

