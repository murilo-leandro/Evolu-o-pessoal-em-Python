import time

tarefas = []

continuar = True
while continuar:
    print("Essas coisas são de uma lista de tarefas, onde você vai:")
    time.sleep(0.5)
    escolha = input("Escolher 1 entre 4 coisas, aqui estão elas: adicionar, remover, listar e sair.").strip().lower()
    if escolha == "adicionar":
        time.sleep(1)
        print(tarefas)
        time.sleep(1)
        escolha_adicionar = input("Arrume aqui qual você deseja adicionar").strip().lower()
        tarefas.append(escolha_adicionar)
        print(tarefas)
        time.sleep(2)
    elif escolha == "remover":
        print(tarefas)
        escolha_remover = input("Escolha qual você deseja remover").strip().lower()
        if escolha_remover in tarefas:
            print("Removido!")
        else:
            print("Não está na lista")
    elif escolha == "listar":
        print(tarefas)
    elif escolha == "sair":
        print("Saindo!")
        continuar = False
    else:
        print("Infelizmente você arrumou errado, deve somente arrumar de forma correta: adicionar, remover, listar e sair. Igual está aqui")
    time.sleep(2)

