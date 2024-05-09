import os 

os.system("cls||clear")

contadorNotas = 0
soma = 0
media = 0 

while True: 
  nota = int(input("Digite uma nota: "))

  if nota > 0:
    soma += nota
    contadorNotas += 1 
  else:
    break

media = soma/contadorNotas



os.system("cls||clear")
print(f"===Exibindo Resultados===")
print(f"A média das notas positivas inseridas é: {media} ")
print(f"A quantidade de notas inseridas: {contadorNotas}")