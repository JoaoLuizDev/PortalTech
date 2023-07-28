"""
3-) Implemente um programa que peça ao usuário para digitar um número e, em seguida, verifique se é um número par ou ímpar. 
Imprima na tela o resultado. 
"""

numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
  print("O número é par.")
else:
  print("O número é ímpar.")
