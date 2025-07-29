def pedido():
    comida = input("Você gostaria de pedir o que? Temos pizza, hamburguer, mas caso quiser sair, diga sair.")
    if comida == "hamburguer":
        print("Uma pizza saindo do forno quentinha ainda.")
    elif comida == "pizza":
        print("Hamburguer saindo na chapa e tudo certinho, já, já na mesa.")
    return comida
continuar = True
while continuar:
    comida = pedido()
    if comida == "sair":
        print("Saindo.")
        continuar = False
