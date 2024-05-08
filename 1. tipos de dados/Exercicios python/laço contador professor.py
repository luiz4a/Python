import os

os.system("cls||clear")

contadorNotas =0
soma = 0
i = 0

while True: 
    nota = float(input(f"Digite uma nota: "))
    resposta = str(input(f"Deseja inserir mais uma nota? (S ou N): "))

    resposta = resposta.upper()

    if resposta !=  "N": 
     soma += nota
     contadorNotas+=1
    else: 
       break

media = soma / contadorNotas 

print(f"A média das notas inseridas é: {media}")