def cafeteria():
    nome = input("Poderia me dizer seu nome?").strip().lower()
    gosto_pessoal = input(f"Por acaso {nome}, o senhor gosta de café?").strip().lower()
    if gosto_pessoal in ["não", "nao", "n"]:
        print("Beleza, eu também não")
    elif gosto_pessoal in ["sim", "s"]:
        print(f"Beleza, então, vou te fazer uma pergunta, {nome}")
    cafe = input(f"{nome}, prefere qual tipo de café? Expresso, coado ou capuccino.").strip().lower()
    if café == "expresso":
        print(f"Realmente, ele é forte, bom gosto, {nome}.")
    elif café == "coado":
        print("Não sei esse, foda-se né?")
    elif café == "capuccino/capucino":
        print("Não sei também.")

cafeteria()
