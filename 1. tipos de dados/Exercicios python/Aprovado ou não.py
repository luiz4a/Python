import os 

os.system("cls||clear")

media = 0 
soma = 0 
situacao = media 

for i in range (0,3): 
 nota = float(input(f"Digite a {i+1}º Nota: "))
 
 soma += nota
 
media = soma/3
 
print(f"A média é: {media}")

if media >= 7:
  print("Aprovado!")
if media < 4:
  print("Voçê está reprovado")


