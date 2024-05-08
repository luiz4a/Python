import os 

os.system("cls|| clear")

pesoMorangos: float
pesoMacas: float
precoMacas: float
precoMorangos: float 
pesoTotal: float


print("\n=== Solicitando Dados ===")
pesoMorangos = float (input("Digite o peso dos morangos (em kg): "))
pesoMacas = float (input ("Digite o peso de macas (em kg): "))
 
if pesoMorangos < 5:
   precoMorangos = 2.50
else: 
   precoMorangos = 2.20

if pesoMacas < 5:
   precoMacas = 1.80
else: 
   precoMacas = 1.50

   pesoTotal = pesoMorangos + pesoMacas
   subtotal = (precoMorangos * pesoMorangos) + ( precoMacas + pesoMacas)

if pesoTotal > 8 or subtotal > 25:
   desconto = subtotal* 0.10
else: 
   desconto = 0 
   totalPagar = subtotal - desconto


print(f"Peso de Morangos: {pesoMorangos}")
print(f"Peso das Maças: {pesoMacas}")
print(f"Soma dos Pesos: {pesoTotal}")
print(f"Subtotal: R${subtotal:.2f}")
print(f"Desconto: R${desconto:.2f}")
print(f"Total a pagar: {totalPagar:.2f}")

