import os 
os. system ("cls")

# Leitura do código da operação
operacao = input("Digite a operação (+, -, *, /): ")

# Leitura dos valores inteiros
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

# Cálculo do resultado
if operacao == "+":
    resultado = A + B
elif operacao == "-":
    resultado = A - B
elif operacao == "*":
    resultado = A * B
elif operacao == "/":
    if B != 0:
        resultado = A / B
    else:
        resultado = "Erro: divisão por zero!"
else:
    resultado = "Operação inválida!"

# Exibir o resultado
print("Resultado:", resultado)
