def verificar_vacina():
    nome = input("Por favor me diga seu nome.").strip().title()
    idade = int(input("Qual sua idade?"))
    condicao_risco = input("Por acaso você tem alguma condição de risco? Escreva somente sim e não.").strip().title()
    if idade >= 60 or condicao_risco == "sim":
        return f"{nome}, você pode tomar a vacina."
    else:
        return f"{nome}, você não pode tomar a vacina."
    terminar = input("Você deseja encerrar? Somente sim e não.").strip().title()

    return terminar

continuar = True
while continuar:
    terminar, mensagem = verificar_vacina()
    print(mensagem)
    if terminar == "sim":
        print("Terminando")
        continuar = False
