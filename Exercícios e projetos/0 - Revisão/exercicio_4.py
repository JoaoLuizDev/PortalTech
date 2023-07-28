"""
4-) Crie um programa que pergunte ao usuário o seu nome e a quantidade de vezes que deseja repetir uma mensagem de 
boas-vindas com o nome digitado.
"""

nome = str(input("Digite seu nome: "))

print(f"Olá, {nome}.")

numero = int(input("Quantas vezes você deseja repetir a mensagem de boas-vindas com o nome digitado? "))

for _ in range(numero):
  print(f"Seja bem-vindo, {nome}.")
"""
