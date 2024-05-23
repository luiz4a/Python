import os 
import time
import sys

def somar (n1,n2):
    resultado = n1 + n2
    return resultado
def multiplicar (n1, n2):
    resultado = n1 * n2
    return resultado
def dividir (n1, n2):
    resultado = n1/n2
    return resultado 
def subtrair (n1,n2):
    resultado = n1 - n2
    return resultado

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

soma = somar( numero1 + numero2)
divisao = dividir (numero1 / numero2)
multiplicacao = multiplicar ( numero1 * numero2)
subtracao = subtrair (numero1 - numero2)

print(f"===Resultados===")
print(f"Os numeros digitados são: {numero1} e {numero2}")
print(f"O resultado da soma é: {soma}")
print(f"O resutado da multiplicação é: {multiplicacao}")
print(f"O resultado da subtração é: {subtracao}")
print(f"O resultado da divisão é: {divisao}")

