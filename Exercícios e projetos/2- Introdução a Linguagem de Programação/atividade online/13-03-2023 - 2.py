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

planta = 0
while planta <= 5:
  if planta == 0 or planta == 2 or planta == 4:
    print(f"regar planta {planta}.")
  planta += 1
