import os 

def cabeçalho():
    os.system("cls||clear")
    print("===SENAI===")
    
def calcularMedias(n1, n2):
    resultado = (n1 + n2) /2
    return resultado 


cabeçalho()
nota1 = float(input("Digite a Primeira nota: "))

cabeçalho()
nota2 = float(input("Digite a Segunda Nota: "))

media = calcularMedias (nota1, nota2)

cabeçalho()
print(f"As Notas inseridas foram: {nota1} e {nota2}")
print(f"A média das notas é: {media}")
