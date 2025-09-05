import os 
os. system ("cls")

# Leitura dos dados do solicitante
renda_mensal = float(input("Digite a sua renda mensal: R$ "))
valor_emprestimo = float(input("Digite o valor do empréstimo solicitado: R$ "))
num_prestacoes = int(input("Digite o número de prestações desejado: "))

# Cálculo do valor da prestação
prestacao = valor_emprestimo / num_prestacoes

# Verificação das condições
limite_emprestimo = 10 * renda_mensal
limite_prestacao = 0.3 * renda_mensal

if valor_emprestimo <= limite_emprestimo and prestacao <= limite_prestacao:
    print("Empréstimo concedido!")
    print(f"Valor da prestação: R$ {prestacao:.2f}")
else:
    print("Empréstimo não concedido.")
    if valor_emprestimo > limite_emprestimo:
        print(f"- O valor solicitado excede o limite permitido (R$ {limite_emprestimo:.2f})")
    if prestacao > limite_prestacao:
        print(f"- O valor da prestação excede 30% da renda mensal (R$ {limite_prestacao:.2f})")
