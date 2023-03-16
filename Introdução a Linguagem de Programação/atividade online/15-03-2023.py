#função em que programa só aceita número inteiro, e informará se o número é menor ou igual a 100, ou maior.

def mostrarnumero():
    numero = int(input("Digite um número menor ou igual a 100: "))
    if 0 <= numero <= 100:
      print(f"O número {numero} é menor ou igual a 100.")
    elif numero < 0:
      print(f"ATENÇÃO. O número {numero} é negativo.")
    else:
      print(f"ERRO. O número {numero} é maior que 100.")
mostrarnumero()

# função para aceitar números decimais.
# para isso, devemos trocar int por float

def mostrarnumero():
    numero = float(input("Digite um número menor ou igual a 100: "))
    if 0 <= numero <= 100:
      print(f"O número {numero} é menor ou igual a 100.")
    elif numero < 0:
      print(f"ATENÇÃO. O número {numero} é negativo.")
    else:
      print(f"ERRO. O número {numero} é maior que 100.")
mostrarnumero()
