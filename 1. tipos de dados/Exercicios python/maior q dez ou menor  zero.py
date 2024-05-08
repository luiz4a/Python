import os

os.system("cls||clear")
 
nota = -1

nota = float(input(f"Digite sua Nota: "))

while  nota < 0 or nota > 10:
 nota = float(input(f"Digite novamente sua Nota(deve estar entre 0 e 10): "))

print(f"Sua Nota é: {nota}")
