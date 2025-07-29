def verificar_par():
    número = int(input("Por favor, arrume um número, diremos se é par ou impar: "))
    if número in [1, 3, 5, 7, 9]:
        print("Esse número é impar")
    elif número in [0, 2, 4, 6, 8, 10]:
        print ("Esse número é par")
    else:("Número invalidado, só trabalhamos até o 10. Melhoraremos em breve")

verificar_par()
