import time

def entrevista():
    nome = input("Poderia me dizer seu nome? ").strip().lower()
    time.sleep(3)
    idade = input(f"{nome}, poderia me dizer sua idade? ").strip().lower()
    time.sleep(3)
    linguagem_programacao = input("Você já estudou programação antes? ").strip().lower()
    time.sleep(1)
    print("Entendo.")
    time.sleep(0.5)
    tipo_programacao = input("Qual linguagem você gostaria de aprender? ").strip().lower()
    time.sleep(3)

    if tipo_programacao == "python":
        print("Ótima escolha. Aliás, sabia que agora, essas perguntas são em Python também, legal, né?")
    time.sleep(2)

    continuacao = input("Bem, já fizemos muitas perguntas. Você deseja continuar? (sim/não) ").strip().lower()
    return continuacao

continuar = True

while continuar:
    resposta = entrevista()
    
    if resposta == "sim":
        print("Beleza, vamos continuar então!\n")
        continuar = True  
    elif resposta in ["não", "nao"]:
        print("Entrevista encerrada. Até a próxima!")
        continuar = False
    else:
        print("Era só sim ou não. Terminaremos por precaução.")
        continuar = False
