import time

print("Lhe darei outros tipos de animais domésticos")
time.sleep(3)
print("cão, gato, pássaro")
time.sleep(2)
animais_domesticos = ["cão", "gato", "pássaro"]
time.sleep(1.5)
nome_animal = input("Adicione outro tipo de animal doméstico: ")
animais_domesticos.append(nome_animal)
time.sleep(1)
print(animais_domesticos)
