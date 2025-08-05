senha_1 = ["dragon123", "dragon12", "dragon1"]
codigo = ["vip123", "vip12", "vip1"]

senha = input("Para entrar na conta, me diga a senha correta. Caso não saber, diga: não sei.").strip().lower()
if senha not in senha_1:
    codigo_alternativo = input("Já que você não sabe a senha ou errou ela. Então me diga um código alternativo para entrar na conta: ").strip().lower()
    if codigo_alternativo not in codigo:
        recuperar = input("Você errou o código e a senha, deseja usar o método para recupera-lá? Use somente sim e não.").strip().lower()
        if recuperar == "sim":
            codigo_senha = input("Método recuperar senha. Deseja usar as senhas ou um código de segunda etapa para acessar a conta? Digite 1 para a senha, 2 para a segunda etapa")
            if codigo_senha == "1":
                print(senha_1)
            elif codigo_senha == "2":
                print(codigo)
    
