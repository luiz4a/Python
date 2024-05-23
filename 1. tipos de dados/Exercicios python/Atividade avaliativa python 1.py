import os
import time
import sys
os.system("clear||cls")

QUANTIDADE_NUMEROS = 5

numeros_inversos = 0
quantidadePares = 0
quantidadeImpares = 0
quantidade_positivos = 0
quantidade_negativos = 0
maior_numero = 0
menor_numero = 99999
soma_pares = 0
soma_impares = 0
soma_geral = 0
numeros = []
mediaPares = 0
mediaImpares = 0
mediaGeral = 0
pares = []
impares = []

for i in range (QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)
    
if numero % 2 == 0:
   quantidadePares += 1
else:
   quantidadeImpares += 1

if pares:
    mediaPares = sum(pares)/len(pares)
else:
    mediaPares = 0

if impares:
    mediaImpares = sum(impares)/len(impares)
else:
    mediaImpares = 0

if numero > 0:
    quantidade_positivos += 1

else:
    quantidade_negativos += 1

if numero > maior_numero:
    maior_numero = numero

if numero < menor_numero:
    menor_numero = numero

soma_geral += numero

# Calculando as médias

mediaGeral = soma_geral / QUANTIDADE_NUMEROS 
numeros_inversos = list(reversed (numeros))

# Imprimindo as estatísticas
os.system("cls||clear")
print("\n===Estatísticas dos números===")
print(f"Quantidade de pares: {quantidadePares}") 
print(f"Quantidade de numeros ímpares: {quantidadeImpares}")
print(f"Quantidade de numeros positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"O maior numero é: {maior_numero}")
print(f"O menor numero é: {menor_numero}")
print(f"A média dos numeros pares é: {mediaPares}")
print(f"A média dos numeros impares é: {mediaImpares}") 
print(f"A média dos numeros inseridos é: {mediaGeral}")
print(f"A quantidade de números inseridos é: {QUANTIDADE_NUMEROS}")
print(f"Os numero em ordem invertida são: {numeros[::-1]}")