import os 
import sys
import time 

os.system("clear||cls")
QUANTIDADE_NUMEROS = 6
numeros = []
impares = 0
pares= 0

for i in range (QUANTIDADE_NUMEROS):
   numero = int(input(f"Digite o {i + 1}º numero:  "))
   numeros.append(numero)

   if numero % 2 == 0:
      pares += 1
   else: 
      impares += 1

print(f"A quantidade de numeros pares é: {pares}")
print(f"A quantidade de números impares é: {impares}")
