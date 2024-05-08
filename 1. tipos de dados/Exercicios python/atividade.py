import os

os.system("cls||clear")

opcao = str
contadorNotas =0
soma = 0
i = 0
media = 0

while (opcao == "S"):
    print("===MENU===")
    print(f"S- Inserir mais uma nota")
    print(f"P- Ver quantas notas foram inseridas") 
    print(f"N- calcular a média das notas")

    opcao = str(input(f"Digite a opção escolhida: "))
    opcao = opcao.upper()

    if opcao == "S": 
     nota = float(input(f"Digite uma nota: "))
     soma += nota
     contadorNotas+=1 
    if opcao == "P":
     print(f"A quantidade de notas inseridas é: {contadorNotas}")  
     opcao == "S"
    if opcao == "N":
      media = soma / contadorNotas 
      print(f"A média das notas inseridas é: {media}")
      print(f"A quantidade de notas inseridas é: {contadorNotas}")