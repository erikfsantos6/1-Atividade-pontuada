import os 
os. system ("cls")

# Leitura da cor do CD
cor = input("Digite a cor do CD (Verde, Azul, Amarelo, Vermelho): ").strip().capitalize()

# Verificação e exibição do preço
if cor == "Verde":
    preco = 10.0
elif cor == "Azul":
    preco = 20.0
elif cor == "Amarelo":
    preco = 30.0
elif cor == "Vermelho":
    preco = 40.0
else:
    preco = None

if preco is not None:
    print(f"O preço do CD {cor} é: R$ {preco:.2f}")
else:
    print("Cor inválida. Por favor, digite Verde, Azul, Amarelo ou Vermelho.")
