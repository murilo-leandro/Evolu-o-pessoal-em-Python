continuar = True

while continuar:
    nome = input("Qual seu nome?").strip().capitalize()
    pedido = input(f"{nome}, deseja pedir algo para si? (sim/não/sair): ").strip().lower()
    if pedido == "sim":
        print("Pedido anotado")
    elif pedido in ["não", "nao"]:
        print("Claro, se mudar de ideia, só chamar.")
    elif pedido == "sair":
        print(f"Encerrando o sistema, boa noite, {nome}!")
        continuar = False
    else:
        print("Por favor, siga as normas que foram ditas.")
