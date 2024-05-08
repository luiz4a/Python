import os 

os.system("cls||clear")

media = 0 
soma = 0 

for i in range (0,4): 
 nota = float(input(f"Digite a {i+1}º Nota: "))
 
 soma += nota
 
media = soma/4

print(f"A média aritmética das notas inserida é: {media}")

