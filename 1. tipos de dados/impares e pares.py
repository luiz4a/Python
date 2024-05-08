import os 

os.system("cls || clear")

pares = 0 
impares = 0 

for i in range (1,6):
  numero = int(input("Digite o {i}º numero: "))
  print(f"{i}")
if numero %2 != 0:
 impares+= i
 print(f"A quantidade de Números impares são: {impares}")
else:
  pares+= i
  print(f"A quantidade de Números Pares são: {pares}")
    