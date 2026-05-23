# Arquivo que recebe a parte de interface
# O validar_interiro serve para não ter ids duplicados

def linha():
    print("=" * 40)

def titulo(texto):
    linha()
    print(texto.center(40))
    linha()

def validar_inteiro(valor, mensagem_erro):
    try:
        return int(valor)
    except ValueError:
        print(mensagem_erro)
        return None


   
