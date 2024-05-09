import os 
os.system("cls||clear")

contadorMulher = 0
maiorIdade = 0
menorIdade = 9999
mediaSalarialM = 0
mediaSalarialF = 0 
quantidadeMulheres = 0
idade = 0
sexo = str
salarioM = 0 
salario = 0

print("===Menu===")
print("1-Adicionar Uma Pessoa")
print("2-Exibir Resultados e sair") 

while True:
 opcao = int(input("Escolha uma opcao do Menu Acima: "))
 idade = int(input("Insira Sua idade: "))
 sexo = str(input("Digite seu sexo (F ou M): "))
 salario = float(input("Digite o seu salario: "))

 sexo = sexo.upper()

 
  if idade > maiorIdade:
      maiorIdade = idade

  if idade < menorIdade:
      menorIdade = idade

 if salarioM > 5000:
      contadorMulher += 1

 
 if opcao == 2:
      print(f"Quantidade de mulheres com salario acima de 5k: {contadorMulher}")
      print(f"A média Salarial das Mulheres é: {mediaSalarialF}")
      print(f"A média Salarial dos Homens é : {mediaSalarialM}")
 break 


  
  
