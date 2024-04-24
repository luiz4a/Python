import os
os.system ("cls || clear")

numero1 = int
numero2 = int 
soma = int
divisao = int 
multiplicação = int 
subtracao = int 

print("Solicitando Dados do Usuario")
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma = numero1 + numero2 
subtracao = numero1 - numero2
multiplicação = numero1 * numero2
divisao = numero1/numero2

os.system(" cls || clear")

print(f"\n===Exibindo Resultados===")
print(f"Os numeros inseridos são: {numero1} e {numero2}")
print(f"O resultado da soma é: {soma}")
print(f"O resultado da subtracao é: {subtracao}")
print(f"O resultado da multiplicação é: {multiplicação}")
print(f"O resultado da divisão é: {divisao}")
