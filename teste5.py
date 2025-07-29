nome = input("Poderia me falar o seu nome, senhor?")
print("Claro, entendido", nome + ", gostariamos de fazer uma pergunta para ti")
programar = input("Por acaso, você gosta de programar? Senhor. (sim/não): "  ).strip().lower()
if programar == "sim":
    print("Incrível, você vai longe assim, continue!")
elif programar == "não":
    print("Que pena, talvez mude no futuro? Quem sabe, né?")
else:
    print("Possivelmente você arrumou errado, use somente sim e não")
