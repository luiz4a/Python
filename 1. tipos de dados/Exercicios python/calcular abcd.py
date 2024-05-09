import os 
os.system("cls||clear")

contadorGeral = 0
contadorPares = 0
mediaGeral = 0
somaPar = 0
somaGeral = 0
mediaPar = 0
numero = 0
contadorImpar  =0
somaImpar= 0 

while True: 
 numero = int(input("Digite um Número(Digite '0' para sair): "))

 if (numero > 0):
        contadorGeral += 1
        somaGeral += numero
        if numero %2 == 0:
         contadorPares += 1
         somaPar += numero
        else: 
         contadorImpar += 1
         somaImpar = 0 
 else: 
    break 
  
mediaGeral = somaGeral/contadorGeral 
if contadorPares != 0:
  mediaPar = somaPar/contadorPares
  
print(f"A média dos numeros é: {mediaGeral}")
print(f"A média dos numero pares é: {mediaPar}")
print(f"A quantidade de numeros pares inseridos é: {contadorPares}")
print(f"A quantidade de numeros impares inseridos são: {contadorImpar}")  

 