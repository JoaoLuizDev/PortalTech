# O que é um array em python?

print("Em Python, um array é uma estrutura de dados que pode armazenar uma coleção de valores.\n"
      "Os elementos de um array em Python são indexados a partir de zero, e podem ser acessados e modificados usando colchetes.")


# Como declarar um array?

lista_numeros = []                  # nome da variável, sinal de atribuição, colchetes

lista_numeros = [3, 19, 54, -2]     # valores, separados por vírgula


# Tipos de dados em array

print("Podemos incluir tipos de dados. Exemplo a seguir.")

lista_int = [1, 2, 3, 4]
lista_floats = [0.3, 3.9, 89.15, 123.45]
lista_strings = ["Eu", "gosto", "de", "panquecas"]
lista_booleanos = [False, True, True, False]


# Array de array

lista_listas = [[1, 2, 3], ['a', 'b', 'c']]

# Imprimindo array na tela

lista_frutas = ['maçã', 'banana', 'pera']
print(lista_frutas)
print("A saída será:\n"
      "['maçã', 'banana', 'pera'].")

# Índices em array

print("Para acessar apenas um item do array, cada item do vetor tem um índice, ou index em inglês.\n"
      "O índice é um valor inteiro que representa cada um dos valores do array, e que começa sempre do número 0 e vai aumentando de 1 em 1.")

lista_frutas = ['maçã', 'banana', 'pera']
"""
'maçã' tem o índice 0
'banana' tem o índice 1
'pera' tem o índice 2
"""

# Imprimindo apenas um valor do array na tela
lista_frutas = ['maçã', 'banana', 'pera']
print(lista_frutas[0])                            # o índice que quiser imprimir deve ficar entre os colchetes

# Criar variável a partir do uso de array
print("Criar uma variável usando um valor do array não altera o array.")

lista_frutas = ['maçã', 'banana', 'pera']
fruta_preferida = lista_frutas[2]
print(fruta_preferida)
print(lista_frutas)
"""
O primeiro print será 'pera'
O segundo print continuará a ser o array ['maçã', 'banana', 'pera']
"""

