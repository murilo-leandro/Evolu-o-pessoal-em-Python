continuar = True
import time

def entrevista():
    nome = input("Primeiramente, poderia me dizer seu nome?").strip().lower()
    time.sleep(2)
    idade = input("Agora, poderia me dizer a sua idade?").strip().lower()
    time.sleep(2)
    função_vida = input("Poderia me dizer se você: estuda, trabalha ou nenhum?").strip().lower()
    time.sleep(2)
    emprego = input("Então, qual profissão você gostaria de ter no futuro?").strip().lower()
    time.sleep(2)
    continuacao = input(f"Essas foram todas as perguntas, agora, {nome} você deseja continuar? (sim/não)").strip().lower()
    if continuacao == "sim":
        print("Continuaremos, repetiremos")
    elif continuacao in["não", "nao"]:
        print("Entrevista encerrada. Boa sorte no seu futuro!")
        continuar = False
    else:
        print("Bem, a resposta foi errado, né?")
entrevista()

