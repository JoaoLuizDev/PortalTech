#resolução do exercício 2

for numero in range (0, 5, 2):
  print(f"Hoje é dia de regar a planta ", numero)

contador = 0
while contador <= 5:
  print(f"Regar planta {contador}.")
  contador += 2
  
for a in range(6):
  if(a % 2 != 0):
    continue
  print('Regar a planta ' + str(a)) 

# Grupo 5 - João Luiz, Thiago e Sandro
