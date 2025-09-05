import os 
os. system ("cls")

morangos = float(input("Digite a quantidade de morangos (Kg): "))
macas = float(input("Digite a quantidade de maçãs (Kg): "))

if morangos <= 5:
    preco_morangos = morangos * 2.50
else:
    preco_morangos = morangos * 2.20

if macas <= 5:
    preco_macas = macas * 1.80
else:
    preco_macas = macas * 1.50

total_kg = morangos + macas
valor_total = preco_morangos + preco_macas

quantidade_total = morangos + macas

if quantidade_total > 10 or total_kg > 15:
    total:float = total_kg * 0.90   # aplica 10% de desconto

print(f"valor a pagar: R$ {total:.2f}")