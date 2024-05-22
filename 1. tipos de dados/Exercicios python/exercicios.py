import os 
os.system("clear||cls")

QUANTIDADE_NOTAS = 3

soma = 0
notas = []

for i in range (QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota: "))

    notas.append(nota)
    soma += nota

    media = sum(notas)/QUANTIDADE_NOTAS

for i in range (QUANTIDADE_NOTAS):
    print(f"Notas: {notas[i]}")

print(f"A média das notas inseridas são: {media}")
