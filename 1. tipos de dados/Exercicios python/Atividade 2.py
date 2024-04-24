import os 
os.system("cls || clear")

nota1 = float
nota2 = float
media = float 
nome = str 
idade = int

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Diigite a segunda nota: "))

media = (nota1 + nota2) /2

os.system("cls||clear")

print(f"===Exibindo Resultados===")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"As notas inseridas são: {nota1} e {nota2}")
print(f"A média das notas é: {media}")