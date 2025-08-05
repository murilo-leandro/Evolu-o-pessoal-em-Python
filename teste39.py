nomes_banidos = ["joão", "joao", "carlos", "carlinhos", "mario"]

senhas_validas = ["carlos1", "carlinhos1", "mario1", "joao1"]
verificacao_bot_impar = ["1", "3", "5", "7", "9"]
verificacao_bot_par = ["0", "2", "4", "6", "8", "10"]

nome = input("Digite seu nome.").strip().lower()

senha = input(f"{nome},me diga a senha correta para entrar na conta.").strip().lower()

if nome not in nomes_banidos and senha in senhas_validas:
    print("Entrada permitida, continue navegando.")
else:
    print("Entrada negada!")
if nome not in nomes_banidos and senha not in senhas_validas:
    tentativa_recuperar = input("Você não está banido, mas pelo visto, a senha está errada. Você deseja recuperar ela? Digite 1 se quiser e 2 para não.")
    tentativa_bot = input("Verificaremos se você é humano. Digite 1 números impar e 1 par, isso dentro de 0-10.")
    if tentativa_bot not in verificacao_bot_impar and not in verificacao_bot_par:
        print("Tentativa falha, interromperemos as tentativas.")
    else:
        print("Correto, mostraremos as senhas.")
        print(senhas_validas)

