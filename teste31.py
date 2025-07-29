nome = input("Qual seu nome?").strip().lower()
idade = int(input(f"Entendido {nome}, poderia me dizer sua idade?"))
ingresso = input("Por acaso você tem um ingresso?").strip().lower()
lista_vip = input("E também, você seu nome está na lista VIP?").strip().lower()
if idade >= 18 and ingresso == "sim":
    print("Você pode entrar.")
elif idade in[16, 17] and lista_vip == "sim":
    print("Sua idade está abaixo, mas está na lista. Pode entrar.")
else:
    print("Você não tem NADA, não pode entrar")
