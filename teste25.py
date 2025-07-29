def bar_de_sucos():
    nome = input("Me diga seu nome.")
    print(f"Entendido senhor {nome}")
    suco = input("Gostaria de algum tipo de suco? Temos de laranja, uva e abacaxi.").strip().lower()
    if suco == "laranja":
        print(f"{nome} este está em falta, nos desculpamos")
    elif suco in["uva", "abacaxi"]:
        print(f"Iremos preparar um suco de {suco} para o senhor")
    else:
        print("Desculpe, nao entendemos, por favor digite corretamente o valor")
    continuacao_programa = input("Temos seu pedido, deseja continuar ou sair?").strip().lower()
    return continuacao_programa
continuar = True
while continuar:
    sair = bar_de_sucos()
    if sair == "sair":
        print("Encerrando.")
        continuar = False
    elif continuacao_programa == continuar:
        print("Continuando, pedidos irão se repetir.")
        continuar = True
    else:
        print("ERRADO, encerrando por segurança do cliente")
        continuar = False
    
