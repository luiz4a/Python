import os 

 #Algoritimo: N�meros de 1 a 10
def cabeçalho():
	os.system("cls||clear")
	print(f"===SENAI===")
	  
cabeçalho()
tabuada = int(input("Digite um numero para ver a sua tabuada: "))
 	
cabeçalho()
print("\nTabuada Completa:", tabuada )

cabeçalho()
for count in range (11):
 print(f"%d x %d = %d" % (tabuada, count, tabuada*count))
 