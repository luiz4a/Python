import os

def cabeçalho():
    os.system("cls||clear")
    print("===SENAI===")

def exibir_tabuada(numero):
    cabeçalho()
    print("\nTabuada Completa:", numero)
    cabeçalho()
    for count in range(11):
        print("%d x %d = %d" % (numero, count, numero * count))

def louise():
    cabeçalho()
    tabuada = int(input("Digite um numero para ver a sua tabuada: "))
    exibir_tabuada(tabuada)

louise() 