import os 
os. system ("cls")

# Leitura das notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Cálculo da média aritmética
media = (nota1 + nota2) / 2

# Exibição da média
print(f"A média do aluno é: {media:.2f}")

# Verificação da situação do aluno
if media >= 6.0:
    print("Parabéns! Você está aprovado!")
elif 4.1 <= media <= 5.9:
    print("Você está em recuperação.")
else:  # media < 4.0
    print("Infelizmente, você está reprovado.")
