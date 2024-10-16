"""
1-) Escreva um programa que solicite ao usuário duas notas e calcule a média. Em seguida, o programa deve imprimir se o 
aluno foi aprovado (média >= 7) ou reprovado (média < 7). 
"""

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
media = (nota_1 + nota_2) / 2

print(f"A média foi de {media}.")
if media >= 7:
  print("O aluno foi aprovado.")
else:
  print("O aluno foi reprovado.")
