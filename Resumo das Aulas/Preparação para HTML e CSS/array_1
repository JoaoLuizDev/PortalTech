# O que é um array em python?

Em Python, um array é uma estrutura de dados que pode armazenar uma coleção de valores.
Os elementos de um array em Python são indexados a partir de zero, e podem ser acessados e modificados usando colchetes.


# Como declarar um array?

lista_numeros = []                  # nome da variável, sinal de atribuição, colchetes

lista_numeros = [3, 19, 54, -2]     # valores, separados por vírgula


# Tipos de dados em array

Podemos incluir tipos de dados. Exemplo a seguir:

lista_int = [1, 2, 3, 4]
lista_floats = [0.3, 3.9, 89.15, 123.45]
lista_strings = ["Eu", "gosto", "de", "panquecas"]
lista_booleanos = [False, True, True, False]


# Array de array

lista_listas = [[1, 2, 3], ['a', 'b', 'c']]


# Imprimindo array na tela

lista_frutas = ['maçã', 'banana', 'pera']
print(lista_frutas)

A saída será: ['maçã', 'banana', 'pera']


# Índices em array

Para acessar apenas um item do array, cada item do vetor tem um índice, ou index em inglês.
O índice é um valor inteiro que representa cada um dos valores do array, e que começa sempre do número 0 e vai aumentando de 1 em 1.

lista_frutas = ['maçã', 'banana', 'pera']

'maçã' tem o índice 0
'banana' tem o índice 1
'pera' tem o índice 2


# Imprimindo apenas um valor do array na tela

lista_frutas = ['maçã', 'banana', 'pera']
print(lista_frutas[0])                            # o índice que quiser imprimir deve ficar entre os colchetes


# Criar variável a partir do uso de array
Criar uma variável usando um valor do array não altera o array.

lista_frutas = ['maçã', 'banana', 'pera']
fruta_preferida = lista_frutas[2]
print(fruta_preferida)
print(lista_frutas)

O primeiro print será 'pera'
O segundo print continuará a ser o array ['maçã', 'banana', 'pera']


# Função len()

As listas podem chegar a ter um número imenso de itens. Nesses casos, como saber quantos elementos esse array possui?
Em Python, a função len(), do inglês length (cumprimento), nos permite saber a quantidade de itens num array.
Para isso, devemos colocar o nome da variável que guarda o array como argumento.

lista_frutas = ['maçã', 'banana', 'pera']
quantidade_frutas = len(lista_frutas)
print(quantidade_frutas)                       # Imprimirá o número 3, pois lista_frutas tem três elementos

Outra forma:

lista_frutas = ['maçã', 'banana', 'pera']
print(len(lista_frutas))                 

Observação: existe uma diferença entre o valor do índice do último elemento de um array, e o valor da quantidade de elementos do mesmo array.

lista_frutas = ['maçã', 'banana', 'pera']       # O valor do índice de 'pera', o último elemento do array, é 2
                                                # O valor do len(lista_frutas) é 3
                                                
                                                
# Percorrer Array
Para percorrer um array pequeno, é simples.

lista_frutas = ['maçã', 'banana', 'pera']
print(lista_frutas[0])
print(lista_frutas[1])
print(lista_frutas[2])

Porém, em um array muito grande, isso seria difícil e cansativo. A solução é usar estrutura de repetição.

lista_frutas = ['maçã', 'banana', 'pera']
for i in range(3):
print(lista_frutas[i])

Na função range acima, começará a imprimir o índice zero até o índice menor que 3.
- Valor inicial do contador = 0
- Condição de parada = contador < 3
- Incremento do contador = 1

Foi necessário escrever o número ‘3’ para a condição de parada, pois, eum array pequeno, fica fácil saber a quantidade de elementos.
E como fazer em um array grande?
Exemplo:

lista_num = [2, 45, 65, 78, 126, 987, 457, 345, 679, 107, 2345, 452, 3, 34, 560]

Uma forma seria contar o número de elementos e depois usar a funççao range().

lista_num = [2, 45, 65, 78, 126, 987, 457, 345, 679, 107, 2345, 452, 3, 34, 560]
for i in range(15):
print(lista_num[i])

Outra forma, mais fácil, é usar a função len() dentro da função range().

Assim, será contado quantos elementos e informa a função range() qual a condição de parada.

lista_num = [2, 45, 65, 78, 126, 987, 457, 345, 679, 107, 2345, 452, 3, 34, 560]
for i in range(len(lista_num)):
print(lista_num[i])


