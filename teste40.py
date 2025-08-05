def verificar_carteira():
    nome = "Marcos"
    idade = 18
    if idade >= 18:
        return f"{nome} pode tirar carteira"
    else:
        return f"{nome} ainda não pode tirar a carteira"

mensagem = verificar_carteira()
print(mensagem)
