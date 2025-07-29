import time

def entrevista():
    
    nome = input("Me fale seu nome.").strip().lower()

    time.sleep(1)
    
    idade = int(input(f"{nome}, agora me diga sua idade."))
    
    time.sleep(1)
    
    pergunta = input("Você gostaria de trabalhar?").strip().lower()
    
    if idade >= 18 and pergunta == "sim":
        hard_skills = input("Entendo, poderia me dizer suas qualidades, isso para que eu queira te contratar.").strip().lower()
        
        time.sleep(1)
        
        nivel_skills = int(input(f"{hard_skills}, nessa sua habilidade, poderia me dizer de 0 a 10 qual nível você se considera?"))
        if nivel_skills in [5, 6, 7]:
            print("Está um pouco abaixo do esperado, mas você pode evoluir")
            
        elif nivel_skills <= 4:
            print("Está muito abaixo do esperado, por favor, dirija-se para a saída!")
            
        elif nivel_skills >= 8:
            print("Ótimo! Seu nível está muito bom, contratado para utilizar sua habilidade conosco!")
            

    elif pergunta in ["nao", "não"] and idade <= 13:
        print("Compreendo seu ponto de vista e ainda a idade. Mas continuaremos o código para que você aprenda no futuro.")

    elif pergunta in ["nao", "não"] and idade >= 18:
        print("Você PRECISA se apressar! Essa idade você precisa de uma renda!!!!")

    elif idade in [17, 16, 15, 14] and pergunta in ["não", "nao"]:
        print("Ok, mas você deveria começar a se preocupar, já está numa idade de começar pensar no futuro.")
        time.sleep(1)
        sair_2 = input("Já que você não quer trabalhar e é menor de idade, gostaria de retirar-se da sala ou vai ficar treinando aqui? Use somente sim ou não").strip().lower()
        if sair_2 == "sim":
            print("Então, retire-se imediatamente")
            return "sim", nome
        
    if idade in [17, 16, 15, 14] and pergunta == "sim":
        menor_aprendiz = input("Você gostaria de ser empregado como menor aprendiz?").strip().lower()
        
        if menor_aprendiz == "sim":
            print("Ótimo! Está contratado para ajudar nas coisas de menor importância!")
        
    sair = input("Bem, com tudo o que temos, você gostaria de retirar-se? Diga apenas sim ou não").strip().lower()
        
    

    return sair, nome

continuar = True
while continuar:
    sair, nome = entrevista()
    if sair == "sim":
        print(f"Secretária, por favor acompanhe o {nome} até a saida")
        continuar = False
    elif sair in ["nao", "não"]:
        print("Entrevista irá continuar.")
    else:
        print("Por favor retire-se imediamente após resposta inadequada")
        continuar = False
    
    
        

    
