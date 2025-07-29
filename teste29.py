import time

filmes = []
continuar = True
while continuar:
    escolha = input("Você pode fazer 4 coisas com a lista: adicionar, remover, lista e sair do programa, decida qual, arrume igual eu arrumei.").strip().lower()
    time.sleep(2)
    if escolha == "adicionar":
        time.sleep(2)
        print(filmes)
        escolha_filme = input("Adicione aqui qual filme você deseja adicionar.")
        filmes.append(escolha_filme)
    elif escolha == "remover":
        print(filmes)
        remover_filme = input("Arrume aqui qual filme você deseja remover.")
        if remover_filme in filmes:
            filmes.remove(remover_filme)
    elif escolha == "lista":
        print(filmes)
    elif escolha == "sair":
        print("Saindo")
        continuar = False
    else:
        print("Errado, só é possível usar: remover, adicionar, lista, sair")
        
