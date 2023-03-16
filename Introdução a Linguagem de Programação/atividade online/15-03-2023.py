"""
Atividade:
- criar uma função que receba um numero menor ou igual a 100
- verificar se o numero é menor ou igual a 100:
- caso o atenda a condição, uma mensagem de parabens e mostrando o numero
- caso o numero seja maior que 100, mostrar uma mensagem de erro

Extra: 
testar se a função aceita numeros do tipo float (decimais) para comparar com o inteiro 100. 
E caso o python não permita comparar int com float. O que pode ser feito para habilitar a comparação entre int e float(decimais)
"""

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
