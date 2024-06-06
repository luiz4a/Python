import os 
import time 
import sys 

def cabeçalho():
    os.system("cls||clear")
    print(f"===MARIERS'CODE===")



while True:
 cabeçalho()
 numero = int(input("Digite o numero para saber o mês do ano: "))
         
 match (numero):
        case 1:
            resultado ='Janeiro'
            break
        case 2:
            resultado ='Fevereiro'
            break
        case 3:
            resultado = 'Março'
            break
        case 4:
             resultado = 'Abril'
             break
        case 5:
            resultado = 'Maio'
            break
        case 6:
            resultado = 'Junho '
            break
        case 7:
            resultado = 'Julho'
            break
        case 8:
            resultado = 'Agosto'
            break 
        case 9:
            resultado = 'Setembro'
            break 
        case 10:
            resultado = 'Outubro'
            break 
        case 11:
            resultado = 'Novembro'
            break 
        case 12:
            resultado = 'Dezembro'
            break
        case _:
            print(f"O numero inserido é inválido!")

print(f"O Mês do ano é: {resultado}")     
