animais = ["cachorro", "gato", "papagaio"]
print(animais)
arrumar = input("Poderia arrumar o nome de outro animal aí?")
animais.insert(3, arrumar)
animais.remove("gato")
animais[1] = "tigre"
print(animais)
