#recebe input de usuario
print("Bem vindo a o hortti sabor!")
nome = input("Ola!! Diga o seu nome por favor:")
print()
endere = input(f"Muito bem {nome}, Digite seu endereço por favor:")
print()
nasc = int(input(f"{nome}, Digite o ano em que voce  nasceu:"))
print()
idade = nasc - 2024
print(f"Voce tem {idade} anos de idade.")
print()

#descriçao das frutas do dia
uva = 10.50
morango = 20.10
melancia = 15.40
banana = 2.75
maca = 4.50
print(f"{nome}, As frutas do dia são as seguintes:")

print(f'''
------------frutas ------ preço/KG-----
<------------------------------->
--{1}---{'uva':2s}----------{uva:5.2f}----
--{2}---{'morango':2s}-------{morango:5.2f}---
--{3}---{'melancia':2s}------{melancia:5.2f}---
--{4}---{'banana':2s}--------{banana:5.2f}----
--{5}---{'maça':2s}----------{maca:5.2f}----
''')

fruta = int(input("escolha o ID da fruta que gostaria de comprar:"))
peso = float(input("Digite a quantidade de KG que você gostaria de comprar:"))

var = True
if fruta == 1:
   valor =  peso*uva
elif fruta == 2:
  valor = peso*morango
elif fruta == 3:
  valor = peso*melancia
elif fruta == 4:
  valor =  peso*banana
elif fruta == 5:
  valor = peso*maca

  valor = fruta*peso

print(f"{nome}, O total da sua conta foi de R${valor:.2f}")

if var == True:
  frete = 4.5
if valor <= 15:
  valor = valor + frete

print(f"{nome}, Voce teve um acrescimo de R${frete:.2f} então o total da sua compra ficou de R$:{valor}")