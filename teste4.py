print("Boa tarde, iremos checar sua temperatura")

temperatura = input("Você está se sentindo bem? (sim/não): ").strip().lower()

if temperatura == "sim":
    print("Continue assim, viva e sobreviva.")
elif temperatura == "não":
    try:
        atual = float(input("Qual é a sua temperatura atual?: "))
        if atual < 38.0:
            print("Sua temperatura está normal.")
        elif 38.0 <= atual <= 40.0:
            print("Você está com febre, procure um médico agora!!")
        else:
            print("Temperatura muito alta! Vá ao hospital imediatamente!")
    except ValueError:
        print("Temperatura inválida. Use apenas números (ex: 37.5).")
else:
    print("Resposta inválida. Por favor, responda com sim ou não.")

