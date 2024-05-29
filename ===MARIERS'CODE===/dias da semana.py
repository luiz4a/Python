import os 
import time 
import sys 

def cabeçalho():
    os.system("cls||clear")
    print(f"===MARIERS'CODE===")



while True:
 cabeçalho()
 numero = int(input("Digite o numero: "))
         
 match (numero):
        case 1:
            resultado ='Domingo'
            break
        case 2:
            resultado ='Segunda'
            break
        case 3:
            resultado = 'Terça'
            break
        case 4:
             resultado = 'Quarta'
             break
        case 5:
            resultado = 'Quinta'
            break
        case 6:
            resultado = 'Sexta'
            break
        case 7:
            resultado = 'Sabádo!'
            break
        case _:
            print(f"O numero inserido é inválido!")

print(f"O dia da semana é: {resultado}")     
if (numero > 1 and numero < 7):
    print(f"É dia útil!")
if (numero == 1):
    print(f"Não é dia útil!") 