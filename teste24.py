def livro():
    escolha = input("Poderia me dizer se você gostaria de: ler, escrever ou até mesmo sair agora.").strip().lower()
    if escolha == "ler":
        print("Beleza, comece a ler, termine o livro em 1 mês. Duvido")
    elif escolha == "escrever":
        print("Essa é uma escolha legal também, termine o que você vai escrever e publique, se der certo, então é sucesso")
    return escolha

continuar = True
while continuar:
    escolha = livro()
    if escolha == "sair":
        print("Beleza, saindo agora mesmo")
        continuar = False
        
