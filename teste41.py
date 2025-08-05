def verifica_doacao():
    nome = input("Me diga seu nome.").strip().lower()
    idade = int(input("Me diga sua idade."))
    peso = float(input("Arrume com ponto, mesmo que o peso sejá um número exato, e, especialmente sem o KG. Qual seu peso?"))
    if 16 <= idade <= 69 and peso >= 50:
        return f"{nome}, {idade}, {peso}. Está tudo correto, você pode doar sangue."
    else:
        return f"{nome}, {idade}, {peso}. Infelizmente você não pode doar sangue."

mensagem = verifica_doacao()
print(mensagem)

