def mostrarnumero():
    numero = int(input("Digite um número menor ou igual a 100: "))
    if 0 <= numero <= 100:
        print("O número é menor ou igual a 100.")
    else:
        print("O número deve ser menor ou igual a 100.")
mostrarnumero()

# para aceitar números decimais, basta trocar int por float
def mostrarnumero():
    numero = float(input("Digite um número menor ou igual a 100: "))
    if 0 <= numero <= 100:
        print("O número é menor ou igual a 100.")
    else:
        print("O número deve ser menor ou igual a 100.")
mostrarnumero()
