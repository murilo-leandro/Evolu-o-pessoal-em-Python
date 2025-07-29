def emprego():
    nome = input("Qual seu nome?")
    idade = int(input(f"{nome}, gostaria de saber sua idade"))
    if idade >= 18:
        print("Beleza, então continuaremos, você é maior de idade")
    else:
        print("Menor de idade, infelizmente, espere até ter a maioridade")
    emprego = input(f"Muito bem senhor {nome}, você acaba por pensar em qual tipo de emprego futuro?")
    print(f"Aqui vai aparecer seus dados e preferências agora:{nome}, {idade}, {emprego}")
    continuacao = input("Você deseja continuar? (sim/não)")
    return emprego

continuar = True
while continuar:
    continuacao = emprego()
    if continuacao in["não", "nao"]:
        continuar = False
