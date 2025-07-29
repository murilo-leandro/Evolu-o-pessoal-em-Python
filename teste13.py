import time
continuar = True

    def carteira_motorista():
    nome = input("Me diga seu nome").strip().lower()
    time.sleep(2)
    idade = int(input(f"{nome}, poderia me dizer sua idade?"))
    if idade >= 18:
        time.sleep(2)
        print("Bem, você é maior de idade, pode fazer uma carteira de motorista")
    elif idade <= 18:
        time.sleep(2)
        print("Bem, você é menor de idade, não pode fazer uma carteira de motorista")
    continuacao = input("Você deseja continuar?").strip().lower()
    if continuacao == "sim":
        print("Beleza")
    if continuacao in ["não", "nao"]:
        print("Terminaremos a sessão")
    continuar = False
carteira_motorista()
