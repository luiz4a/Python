import os 

os.system("cls||clear")

resultado = False 

def cabecalho():
 os.system("cls||clear")
 print(f"===MARIERS'CODE===")

cabecalho()
while True:
 a = int(input("Digite o primeiro numero: "))
 if ( a >= 0):
   break
while True:
 b = int(input("Digite o segundo número: "))
 if ( b >=0):
     break
while True:
    operador = input("Digite o operador (+ - * /):  ")
    if(operador == "+" or operador == "-" or operador == "*" or operador == "/"):
      break

match (operador):
     case '+':
      resultado = a + b
     case '-':
      resultado = a - b
     case '*':
      resultado = a * b
     case '/':
      resultado = a / b
     
cabecalho()
print(f"Operador escolhido: {operador}")
print(f"Numeros digitados: {a} e {b}")
print(f"O resultado da operação é: {resultado}")
