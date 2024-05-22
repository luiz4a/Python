import os 
import sys
import time 

os.system("clear||cls")

numeros = []
menorNumero = sys.maxsize
maiorNumero = 0

numero = int(input("Digite uma nota (ou 0 para sair): "))
while numero != 0:
    numeros.append(numero)
    maiorNumero = max(numeros)
    menorNumero = min(numeros)
    numero = int(input("Digite uma nota (ou 0 para sair): "))

print(f"O maior número é: {maiorNumero}")
print(f"O menor número é: {menorNumero}")
