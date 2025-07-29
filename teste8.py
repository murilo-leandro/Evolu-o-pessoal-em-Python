continuar = True

while continuar:
    nome = input("Qual seu nome?")
    pedido = input("Gostaria de pedir alguma coisa? (sim/não/encerrar)")
    if pedido == "sim":
        print("OK, pedido anotado. Espere")
    elif pedido == "não":
        print("Certo, sem problemas")
    elif pedido == "encerrar":
        print("Encerrando o atendimento.")
        continuar = False
    else:
        print("Não entendi, digite entre as normas pedidas")
