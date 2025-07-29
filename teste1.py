print("O F5 deu merda, OHHH!!")
F5 = False

if F5 == False:
    print("Errado, conserte isso")
else:
    print("Perfeito, continue assim")

if F5 == False:
    resposta = input("Você já resolveu o problema? (sim/não): ").strip().lower()
    if resposta == "sim":
        print("Ainda bem, podemos continuar agora")
    elif resposta == "não":
        print("Que pena, continua tentando, você consegue.")
        resposta = input("Você está demorando, gostaria de uma ajudinha, de boa? (sim/não): ")
    else:
        print("Infelizmente você arrumou errado, que pena.")
