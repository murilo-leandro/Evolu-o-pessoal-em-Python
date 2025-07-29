import time

def banco():
    pedido = input("Boa tarde, gostaria de pedir o que? Temos 3 coisas: saldo, saque e sair.").strip().lower()
    if pedido == "saldo":
        print("R$0,00")
    elif pedido == "saque":
        saque = int(input("Por favor, insira um valor em números aqui."))
        print(f"{saque}, o saque foi feito.")
    return pedido
continuar = True    
while continuar:
    pedido = banco()
    if pedido == "sair":
        print("Pronto, sairemos")
        continuar = False
        
        
