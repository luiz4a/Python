import os 

def cabeçalho():
 os.system("cls||clear")
 print("===CARDÁPIO===")


cabeçalho()
print(f" 1 - PICANHA R$25,00")
print(f" 2 - LASANHA R$20,00")
print(f" 3 - STROGONOFF R$18,00")
print(f" 4 - BIFE ACEBOLADO R$15,00")
print(f" 5 - PÃO COM OVO R$5,00")
 
while True:
    codigo = int(input("Digite um dos codigos apresentados: "))
    
    match (codigo):
        case 1:
            pratoEscolhido = 'Picanha'
            valor = '25,00'
        case 2:
            pratoEscolhido = 'Lasanha'
            valor = '20,00'
        case 3:
            pratoEscolhido =  'Strogonoff'
            valor = '18,00'
        case 4:
            pratoEscolhido = 'Bife Acebolado'
            valor = '15,00'
        case 5:
            pratoEscolhido = 'Pão com ovo'
            valor = 5,00
        case _:
            print(f"Código inválido!")
    break 

print(f"O prato escolhido é: {pratoEscolhido}")
print(f"O valor do prato é: {valor}")