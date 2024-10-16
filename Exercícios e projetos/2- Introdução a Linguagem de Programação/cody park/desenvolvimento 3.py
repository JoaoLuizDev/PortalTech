"""
Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

Escreva um código que imprima todos os números exceto o número 13.
Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.

Como desafio, imprima eles em ordem decrescente (20, 19, 18...)
"""

print("Usando laço for in range, pulando 13º andar.")
for hotel in range (1, 21, 1):
  if 1 <= hotel < 13:
    print(str(hotel) + "º andar.")
  elif hotel >= 14:
    print(str(hotel) + "º andar.")

print("-*--*--*--*--*--*--*--*--*--*--*--*--*-")
print("Outro modo de usar for in range.")
for num in range (1, 21):
  if num != 13:
    print(str(num) + "º andar.")
  
print("-*--*--*--*--*--*--*--*--*--*--*--*--*-")
print("Usando laço while, pulando 13º andar.")
numero = 0
while numero <= 20:
  if 1 <= numero < 13:
    print(str(numero) + "º andar.")
  elif numero >= 14:
    print(str(numero) + "º andar.")
  numero += 1

print("-*--*--*--*--*--*--*--*--*--*--*--*--*-")
print("Outro modo de usar o laço while.")
andarhotel = 0
while andarhotel <= 20:
  if andarhotel != 13:
    print(str(andarhotel) + "º andar.")
  andarhotel += 1

print("-*--*--*--*--*--*--*--*--*--*--*--*--*-")
print("Ordem descrescente, pulando 13º andar.")
for n in range (20, 0, -1):
  if n != 13:
    print(str(n) + "º andar.")

print("-*--*--*--*--*--*--*--*--*--*--*--*--*-")
print("Outra forma de escrever o código.")
for andar in range (20, 0, -1):
  if andar >= 14:
    print(str(andar) + "º andar.")
  elif 1 <= andar < 13:
    print(str(andar) + "º andar.")
