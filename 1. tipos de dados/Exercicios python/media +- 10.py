import os

os.system("cls||clear")
 
nota1= -1
nota2 = -1


while nota1 < 0 or nota1 > 10:
 nota1 = float(input(f"Digite sua Primeira Nota(deve estar entre 0 e 10): "))

while nota2 < 0 or nota2 > 10:
 nota2 = float(input(f"Digite novamente sua Nota(deve estar entre 0 e 10): "))


os.system("cls||clear")
media = (nota1 + nota2)/2          
print(f"Sua Primeira nota é: {nota1}")
print(f"Sua Segunda nota é: {nota2}")
print(f"Sua Média é: {media}")