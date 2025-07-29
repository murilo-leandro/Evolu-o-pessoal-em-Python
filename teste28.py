lista_compras = []

continuar = True

while continuar:

    opcoes_demais = input("O que você deseja fazer? É possível usar: adicionar, remover, ver e sair. Digite como eu arrumei.").strip().lower()
    if opcoes_demais == "adicionar":
        desejo = input("O que você deseja adicionar?").strip().lower()
        lista_compras.append(desejo)
        
    if opcoes_demais == "remover":
        print(lista_compras)
        desejo_remover = input("Escolha o que você deseja remover.").strip().lower()
        if desejo_remover in lista_compras
            lista_compras.remove(desejo_remover)
        else:
            print("Item nao está na lista")
        
    if opcoes_demais == "ver":
        print(lista_compras)
        
    elif opcoes_demais == "sair":
        print("Saindo.")
        continuar = False

    else:
        print("Provavelmente você errou, que pena.")
