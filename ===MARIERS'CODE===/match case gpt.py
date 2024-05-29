import os

os.system("cls||clear")

def cabecalho():
    os.system("cls||clear")
    print("===MARIERS'CODE===")

while True:
    cabecalho()
    a = int(input("Digite o primeiro numero: "))
    operador = input("Digite o operador (+ - * /): ")
    b = int(input("Digite o segundo número: "))

    resultado = False

    match operador:
        case '+':
            resultado = a + b
        case '-':
            resultado = a - b
        case '*':
            resultado = a * b
        case '/':
            resultado = a / b
        case _:
            cabecalho()
            print("Operador inválido!")
            reiniciar = input("Deseja fazer outra operação? (s/n): ")
            if reiniciar.lower() != 's':
                break
            else:
                print(f"O resultado é: {resultado}")

    cabecalho()
    print(f"Operador escolhido: {operador}")
    print(f"Números digitados: {a} e {b}")
    if resultado is not False:
        print(f"O resultado da operação é: {resultado}")
