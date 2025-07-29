import time

def evento():
    nome = input("Poderia me dizer seu nome?").strip().lower()
    time.sleep(1)
    ingresso = input(f"Entendido {nome}, por acaso tem o ingresso do evento?").strip().lower()
    time.sleep(1)
    funcionaria = input("Aliás, só para confimar. Você é funcionário do evento?").strip().lower()
    if ingresso == "sim" or funcionaria == "sim":
        print("Perfeito, você pode entrar agora")
    else:
        print("Errado, por favor faça direito. Obrigado.")

evento()
