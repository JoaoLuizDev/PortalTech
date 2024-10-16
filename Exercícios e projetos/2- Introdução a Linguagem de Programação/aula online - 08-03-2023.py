# criando variáveis
bebida = "coca-cola"
comida = "pizza"
valorbebida = 10
valorpizza = 30
alcoolica = "não é alcoólica"

# imprimindo valor das variáveis
print(bebida)
print(comida)

# unindo variáveis
gastototal = valorbebida +  valorpizza
print(gastototal)

# criar frase com variável embutida
print(f"Minha bebida favorita é {bebida}.")
print(f"Ela custa {valorpizza} reais e {alcoolica}.")
print(f"Minha comida favorita é {comida}.")
print(f"Ela custa {valorpizza}.")

from math import floor
print(f"O gasto para comprar sua bebida e comida favorita será de {gastototal} reais.")
orçamento = float(input("Qual seu orçamento em reais para fazer a comprar? "))
if orçamento > gastototal:
  quantidade = orçamento / gastototal
  arredondar = floor(quantidade)
  print(f"É possível comprar {arredondar} das suas bebidas favoritas.")
else:
  print("Não é possível comprar sua bebida favorita com seu orçamento atual.")
