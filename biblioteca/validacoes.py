# Arquivo criado para fazer as validações 

def validar_texto(mensagem, campo_nome):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print(f"Erro: O campo '{campo_nome}' não pode ficar vazio.")

def validar_ano(mensagem):
    while True:
        valor = input(mensagem).strip()
        try:
            ano = int(valor)
            if ano <= 0:
                print("Erro: O ano deve ser maior que zero.")
                continue
            return ano
        except ValueError:
            print("Erro: Digite um ano válido (apenas números).")
