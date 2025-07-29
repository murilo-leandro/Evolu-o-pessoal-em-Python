continuar = True

while continuar:
    numero = input("Digite um número de 1 até 5. Um aviso, não vale números decimais: ").strip()
    
    if numero == "3":
        print("Infelizmente, você errou. Haha.")
    elif numero == "4":
        print("Infelizmente, você acertou. Parabéns.")
    elif numero == "5":
        print("Infelizmente, você errou. Haha.")
    elif numero == "1":
        print("Infelizmente, você errou. Haha.")
    elif numero == "2":
        print("Infelizmente, você errou. Haha.")
    else:
        print("Número inválido. Tente de novo.")
    parar_continuar = input("Usuário, você deseja parar, ou continuar? (parar/continuar): ").strip().lower()
    if parar_continuar == "parar":
        print("Beleza, parado")
        continuar = False
    elif parar_continuar == "continuar":
        print("Com certeza, continuaremos")
    else:
        print("Resposta inválida, vamos continuar mesmo assim.")
