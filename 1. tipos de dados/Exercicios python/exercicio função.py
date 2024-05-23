import os



def cabeçalho():
    os.system("cls||clear")
    print("====MARIERS'CODE====")


def par_ou_impar (numero):
    if numero % 2 == 0:
       return "par"
    else:
       return "impar"

cabeçalho()    
numero = int(input("Digite um numero: "))   

cabeçalho()
resultado = par_ou_impar (numero)
print(f"O número {numero} é {resultado}.")
