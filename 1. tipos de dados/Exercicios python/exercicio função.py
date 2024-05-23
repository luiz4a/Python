import os


def cabeçalho():
    os.system("cls||clear")
    print("====MARIERS'CODE====")

def verificar_impares (numeros):
    impares = 0
    for numero in numeros :
     if numero % 2 != 0:
       impares += 1
    return impares

def verificar_pares (numeros):
    pares = 0
    for numero in numeros: 
     if numero % 2 == 0:
       pares += 1
    return pares
     
QTD = 6
lista_numeros = []

cabeçalho()
for i in range(QTD):
    numero = int(input("Digite um numero: "))   
    lista_numeros.append(numero)
     

quantidade_pares = verificar_pares (lista_numeros)
quantidade_impares = verificar_impares (lista_numeros)


cabeçalho()
print(f"Quantidade de numeros impares: {quantidade_impares}")
print(f"Quantidade de pares é: {quantidade_pares}")
