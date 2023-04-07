# Array

## O que é um array em python?

Em Python, um array é uma estrutura de dados que pode armazenar uma coleção de valores.
Os elementos de um array em Python são indexados a partir de zero, e podem ser acessados e modificados usando colchetes.


## Como declarar um array?

lista_numeros = [ ] <br>                  
* nome da variável, sinal de atribuição, colchetes <br>
lista_numeros = [3, 19, 54, -2] <br>     
* valores, separados por vírgula


## Tipos de dados em array

Podemos incluir tipos de dados. Exemplo a seguir:

lista_int = [1, 2, 3, 4] <br>
lista_floats = [0.3, 3.9, 89.15, 123.45] <br>
lista_strings = ["Eu", "gosto", "de", "panquecas"] <br>
lista_booleanos = [False, True, True, False]


## Array de array

lista_listas = [[1, 2, 3], ['a', 'b', 'c']]
<br>

## Imprimindo array na tela

lista_frutas = ['maçã', 'banana', 'pera'] <br>
print(lista_frutas)                       
<br>
A saída será: ['maçã', 'banana', 'pera']


## Índices em array

Para acessar apenas um item do array, cada item do vetor tem um índice, ou index em inglês. <br>
O índice é um valor inteiro que representa cada um dos valores do array, e que começa sempre do número 0 e vai aumentando de 1 em 1.

lista_frutas = ['maçã', 'banana', 'pera']

'maçã' tem o índice 0 <br>
'banana' tem o índice 1 <br>
'pera' tem o índice 2


## Imprimindo apenas um valor do array na tela

lista_frutas = ['maçã', 'banana', 'pera'] <br>
print(lista_frutas[0]) <br>
* o índice que quiser imprimir deve ficar entre os colchetes


## Criar variável a partir do uso de array

Criar uma variável usando um valor do array não altera o array. <br>

lista_frutas = ['maçã', 'banana', 'pera'] <br>
fruta_preferida = lista_frutas[2] <br>
print(fruta_preferida) <br>
* saída: 'pera' <br>
print(lista_frutas) <br>
* saída: ['maçã', 'banana', 'pera']


## Função len()

As listas podem chegar a ter um número imenso de itens. Nesses casos, como saber quantos elementos esse array possui? <br>
Em Python, a função len(), do inglês length (cumprimento), nos permite saber a quantidade de itens num array. <br>
Para isso, devemos colocar o nome da variável que guarda o array como argumento.

lista_frutas = ['maçã', 'banana', 'pera'] <br>
quantidade_frutas = len(lista_frutas) <br>
print(quantidade_frutas) <br>                      
* Imprimirá o número 3, pois lista_frutas tem três elementos

Outra forma:

lista_frutas = ['maçã', 'banana', 'pera'] <br>
print(len(lista_frutas)) <br>                

Observação: existe uma diferença entre o valor do índice do último elemento de um array, e o valor da quantidade de elementos do mesmo array. <br>

lista_frutas = ['maçã', 'banana', 'pera'] <br>
* O valor do índice de 'pera', o último elemento do array, é 2 <br>
* O valor do len(lista_frutas) é 3
                                                
                                                
## Percorrer Array

Para percorrer um array pequeno, é simples. <br>

lista_frutas = ['maçã', 'banana', 'pera'] <br>
print(lista_frutas[0]) <br>
print(lista_frutas[1]) <br>
print(lista_frutas[2]) <br>

Porém, em um array muito grande, isso seria difícil e cansativo. A solução é usar estrutura de repetição. <br>

lista_frutas = ['maçã', 'banana', 'pera'] <br>
for i in range(3): <br>
print(lista_frutas[i]) <br>

Na função range acima, começará a imprimir o índice zero até o índice menor que 3. <br>
- Valor inicial do contador = 0 <br>
- Condição de parada = contador < 3 <br>
- Incremento do contador = 1 <br>

Foi necessário escrever o número ‘3’ para a condição de parada, pois, eum array pequeno, fica fácil saber a quantidade de elementos. <br>
E como fazer em um array grande? <br>
Exemplo: <br>

lista_num = [2, 45, 65, 78, 126, 987, 457, 345, 679, 107, 2345, 452, 3, 34, 560] <br>

Uma forma seria contar o número de elementos e depois usar a funççao range(). <br>

lista_num = [2, 45, 65, 78, 126, 987, 457, 345, 679, 107, 2345, 452, 3, 34, 560] <br>
for i in range(15): <br>
print(lista_num[i]) <br>

Outra forma, mais fácil, é usar a função len() dentro da função range(). <br>

Assim, será contado quantos elementos e informa a função range() qual a condição de parada. <br>

lista_num = [2, 45, 65, 78, 126, 987, 457, 345, 679, 107, 2345, 452, 3, 34, 560] <br>
for i in range(len(lista_num)): <br>
print(lista_num[i])


## Alterar um dado usando índice

Substituir um dos elementos na lista abaixo: <br>
lista_frutas = ['maçã', 'banana', 'pera'] <br>

Informamos que o índice 0 em lista_frutas é 'melancia'. <br>

lista_frutas[0] = 'melancia' <br>
print(lista_frutas) <br>

Será impressoO: ['melancia', 'banana', 'pera']


## Alterar mais de um dado usando índices

Na lista a seguir: <br>
lista_frutas = ['melancia', 'banana', 'pera'] <br>

Para alterar dois elementos, por exemplo, podemos acessar mais de um item por vez, separando eles por vírgulas e usando um único operador de atribuição: <br>
lista_frutas[1], lista_frutas[2] = 'morango', 'abacaxi' <br>
print(lista_frutas) <br>

Será impresso: ['melancia', 'morango', 'abacaxi'] <br>

Podemos atribuir o valor de um elemento do array, a outro elemento do mesmo array. <br>

Na lista a seguir: <br>
lista_frutas = ['melancia', 'morango', 'abacaxi'] <br>

Atribuímos ao índice 1 o mesmo valor do índice 0. <br>
lista_frutas[1] = lista_frutas[0] <br>
print(lista_frutas) <br>
Será impresso: ['melancia', 'melancia', 'abacaxi']


## Adicionar elementos

Usamos a função append(), que significa “anexar”. <br>
Devemos escrever o nome do array ao qual queremos adicionar um item, seguido de um ponto ‘.’, o nome da função, e o item a ser adicionado dentro dos parênteses.
<br>
Exemplo: <br>

lista_frutas = ['melancia', 'morango', 'abacaxi'] <br>

lista_frutas.append('kiwi') <br>
print(lista_frutas) <br>
Será impresso: ['melancia', 'morango', 'abacaxi', 'kiwi'] <br>

O elemento adicionado será o último na lista.


## Remover último elemento de um array

Usamos a função pop(). Não é preciso preencher os parêntese, porque a função remove o último elemento. <br>

lista_frutas = ['melancia', 'morango', 'abacaxi', 'kiwi'] <br>

lista_frutas.pop() <br>
print(lista_frutas) <br>
Será impresso: ['melancia', 'morango', 'abacaxi']
