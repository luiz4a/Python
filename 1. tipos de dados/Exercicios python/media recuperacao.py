import os

os.system("cls||clear")
 
os.system("clear")
TAM = 3
soma = 0
for i in range (TAM):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota (entre 0 e 10): "))

        if nota < 0 or nota > 10:
            print("Nota inválida. Por favor, tente novamente. \n")
        else:
            soma += nota
            break   

media = soma / TAM
if media > 7:
 print(f"Aprovado!")
elif media > 5 or media < 6.9:
 print(f"Voçê está em recuperação!")
else:
  print(f"Você foi Reprovado")

print(f"Sua Média é: {media}")
    