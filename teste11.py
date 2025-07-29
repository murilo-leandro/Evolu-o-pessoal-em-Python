import time

continuar = True

while continuar:
    nome = input("Poderia me dizer seu nome?").strip().lower()
    emprego = input(f"Muito bem {nome}, poderia me falar qual seu emprego futuro?").strip().lower()
    futuro = input(f"Ótimo, para esse emprego, você já está trabalhando, ou cursando, para no futuro ser um {emprego}?").strip().lower()
    if emprego == "médico":
        print("Bela profissão, mas ainda muito difícil")
    if futuro == "sim":
        print("Continue assim, sonhe no futuro")
    if futuro in ["não", "nao"]:
        print("Tente começar agora, um começo difícil e cedo, do que um despertar tardio")
    time.sleep(5)
    print(f"{nome}, {emprego}, {futuro}. Essas são todas as perguntas e respostas que fiz agora, se existe algo ruim, repense, e melhore, mas continue bom ainda.")
    time.sleep(4)
    finalizar = input("Depois de tudo, se deseja terminar a entrevista, digite encerrar, se não, vai ficar em loopíng").strip().lower()
    if finalizar == "encerrar":
        print("Encerrado, se quiser de novo, reinicie o sistema do Python")
        continuar = False
