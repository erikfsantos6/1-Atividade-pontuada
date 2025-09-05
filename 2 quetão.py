import os 
os. system ("cls")

# Leitura dos dados
nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (Masculino/Feminino): ")
estado_civil = input("Digite seu estado civil: ")

tempo_casada = input("digite a duração do casamento:")

if sexo == "F" and estado_civil == "CASADA":
 casamento = int(input("duração do casamento")) 
else:
    tempo_casada = None
 

print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")
print(f"duração do casamento:(casada) ")



if tempo_casada is not None:
    print(f"Tempo de Casada: {tempo_casada} anos")
