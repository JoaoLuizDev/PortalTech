"""
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando 
até que um valor correto seja preenchido.
"""

import datetime

print("Olá, seja bem-vindo.")
nome = input("Digite seu nome: ")
print(f"Olá, {nome}.")
ano = None
while ano is None or not (1922 <= ano <= 2022):
  try:
    ano = int(input("Digite o ano de seu nascimento com 4 dígitos: "))
    if not (1922 <= ano <= 2022):
      print("Ano de nascimento inválido. Tente novamente.")
  except ValueError:
    print("Ano de nascimento inválido. Tente novamente.")1
atual = datetime.datetime.now().year
idade = atual - ano
print(f"{nome}, sua idade é de {idade} anos.")
