import os 
import sys
import time 

os.system("clear||cls")

QUANTIDADE_NUMEROS = 5
numeros = []
menorNumero = sys.maxsize
maiorNumero = 0

for i in range(QUANTIDADE_NUMEROS):
 numero = int(input("Digite uma nota: "))
 numeros.append(numero)
 maiorNumero = max(numeros[i], maiorNumero)
 menorNumero = min(numeros[i],menorNumero)

print(f"O maior número é: {maiorNumero}")
print(f"O menor número é: {menorNumero}")
