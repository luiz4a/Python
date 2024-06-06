import os 
import time 
import sys 

desconto = 0 
precoFinal = 0
PrecoParcelado = 0

def cabeçalho (): 
    os.system("cls||clear")
    print("===MARIERS'CODE===")

cabeçalho()
precoProduto = float(input("Digite o valor do produto:  "))

cabeçalho()
print(f"Selecione  a forma de pagamento")
print(f" 1 | Pagamento A vista")
print(f" 2 | Pagamento Parcelado")
opcao = int(input("Digite A forma que deseja pagar: "))

match (opcao):
    case 1:
        desconto = precoProduto * 0.10
        preco_final = precoProduto - desconto
        cabeçalho()
        print(f"\nPreço do produto: R$ {precoProduto}")
        print(f"Forma de pagamento: a vista")
        print(f"Valor do desconto: R$ {desconto}")
        print(f"Total a pagar: R$ {preco_final}")
    case 2:
        parcelas = int(input("\nDigite a quantidade de parcelas: "))

        precoParcelado = precoProduto / parcelas
        preco_final = precoProduto
        cabeçalho()
        print(f"\nPreço do produto: R$ {precoProduto}")
        print(f"Forma de pagamento: a prazo")
        print(f"Quantidade de parcelas: {parcelas}")
        print(f"Valor por parcela: R$ {precoParcelado}")
        print(f"Total a prazo: R$ {preco_final}")
    case _:
        print("Opção inválida! \n")
