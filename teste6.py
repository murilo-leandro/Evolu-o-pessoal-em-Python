def atendimento():
    nome = input("Poderia me responder o qual é o seu nome?")
    duvida = input(f"Muito bem, {nome}. Por acaso você tem alguma dúvida sobre: Python, Java ou nenhuma?").strip().lower()
    if duvida == "python":
        print("Ah, muito bem. Aliás, essa é a linguagem que você está usando")
    elif duvida == "java":
        print("Muito bem também, essa é ótima, pode ser utilizado para tudo")
    elif duvida == "nenhuma":
        print("Pena né, mas fazer o que, tente aprender alguma")
    else:
        print("Provavelmente você fez errado para essa mensagem aparecer, reinicie o programa para fazer de novo")
atendimento()
