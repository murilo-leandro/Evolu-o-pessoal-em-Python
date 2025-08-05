nome = input("Qual seu nome?").strip().lower()
nota = int(input("Qual sua nota?"))
entrega_trabalho = input("Você entregou a atividade?").strip().lower()

if nota >= 7 and entrega_trabalho == "sim":
    print("Parabens! passou direto de ano.")
elif nota in [5, 6] and entrega_trabalho == "sim":
    print(f"{nome}, você está de recuperação, mas com esforço é possível passar.")
elif nota <= 6 and entrega_trabalho in ["nao", "não"]:
    print("Infelizmente, você reprovou por nota e falta de cooperação com as atividades.")
