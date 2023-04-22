cadastro = 0

print("Cadastro de lutadores.")
while cadastro < 5:
  nome = str(input("Digite o nome do lutador. "))
  peso = float(input("Digite o peso do lutador em kg. "))
  if peso <= 57:
    print(f"O lutador {nome} pertence à categoria PESO PENA.")
  elif peso <= 73:
    print(f"O lutador {nome} pertence à categoria PESO MÉDIO.")
  else:
    print(f"O lutador {nome} pertence à categoria PESO PESADO.")
  print("--------------------------------------------")
  cadastro = cadastro +1
