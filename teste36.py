nome = input("Poderia me dizer o seu nome?").strip().lower()
idade = int(input(f"Certo {nome}, agora por favor me diga sua idade"))
convite = input("Por acaso você tem um convite para entrar?").strip().lower()
lista_vip = input("Aliás, você estaria na lista VIP para entrar?").strip().lower()

if convite in ["nao", "não"] and idade >= 18:
    dinheiro = input("Você gostaria de comprar com dinheiro agora?").strip().lower()
    if dinheiro == "sim":
        print("Certo, já está pago, pode aproveitar a festa!")
    elif dinheiro in ["nao", "não"]:
        print("Tranquilo, retire-se então.")
        
elif convite == "sim" and idade >= 18:
    print("Beleza, pode entrar direto.")
    
elif lista_vip == "sim" or idade in [16, 17]:
    print("Pode entrar.")
