def conta():
    nome = input("Deseja registrar qual nome?").strip().lower()
    conta = input(f"Bem vindo {nome}, por acaso você tem uma conta de e-mail?").strip().lower()
    if not conta == "sim":
        print("Cadastro realizado com sucesso!")
    else:
        print("Você já tem uma conta!")

conta()
