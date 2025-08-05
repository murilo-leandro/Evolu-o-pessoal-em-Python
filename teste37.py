banidos = ["joão", "ronaldo fenômeno", "renato cariani", "rodolfo", "czewsntoysz"]

nome = input("Por favor digite seu nome.").strip().lower()
credencial = input("Por acaso você tem uma credencial de acesso?").strip().lower()
if nome not in banidos:
    print(f"Acesso liberado, {nome}")
else:
    print(f"Acesso negado, {nome}")
    
