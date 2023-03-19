"""
Funções

As funções em programação e o refrão de uma música têm algumas semelhanças interessantes. O refrão é uma parte da música 
que é repetida várias vezes. Da mesma forma, uma função é um bloco de código que é escrito uma vez e pode ser chamado 
várias vezes de diferentes partes do programa.

Em Python, uma função é um bloco de código que executa uma tarefa específica quando é chamado. As funções são usadas 
para dividir um programa em partes menores e mais gerenciáveis, tornando o código mais organizado, legível, além de reduzir 
a duplicação de código. 

Uma função é definida com a palavra-chave "def", seguida do nome da função e um conjunto de parênteses, que podem incluir 
parâmetros, e terminada com um sinal de dois pontos. O código que pertence à função é indentado em relação à definição da função.

Exemplo:
def soma(x, y):
    resultado = x + y
    return resultado

A estrutura de uma função é composta por três elementos.

- Nome da função: é interessante ter um nome que defina a tarefa da função. Por ele que a função é chamada no meio do código;
- Parâmetros: é necessário informar quais valores serão utilizados na função, pois eles podem ser usados de acordo com a situação, ficando diferentes;
- Resposta (retorno): a função deve retornar o resultado da sua operação ao terminar a execução.

"""
# praticando

def soma(x, y):
    resultado = x + y
    return resultado

resultado = soma(54, 97)
print(resultado)
print(f"O valor da soma será de {resultado}.")

print("*--*" * 10)
def media(x, y):
    resultado = (x + y) / 2
    return resultado

resultado = media(54, 97)
print(resultado)
print(f"A média é igual a {resultado}.")

"""
Por que usar função?

Imagine um código que repita a operação a seguir diversas vezes:

media = (nota1 + nota2 + nota3 + nota4) / 4
print("A média é:", media)

Em todas elas, deveria ser digitado o cálculo da média, indicando ao computador como realizar a operação.

Ao definirmos a função para realizar o cálculo, basta chama-la usando os argumentos, em vez de repetir o 
cálculo em cada lugar onde precisamos da média. Isso torna o código muito mais legível e organizado, 
além de economizar tempo de digitação e minimizar a chance de erros.

def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    return media

media = calcular_media(nota1, nota2, nota3, nota4)
print("A média é:", media)
"""

#praticando
print("*--*" * 10)

def calcular_media(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    return media

media = calcular_media(8, 6, 7, 2)
print("A média é:", media)

media = calcular_media(3, 4, 9, 1)
print("A média é:", media)

media = calcular_media(5, 6, 6, 5)
print("A média é:", media)

"""
Imprimir o resultado dentro da própria função através da função print() não é uma boa prática, pois o objetivo das funções é,
apenas, executar um procedimento e retornar o resultado.  

Na linguagem Python, é possível retornar mais de um valor na função, basta separar os valores por vírgula quando for receber 
o valor do retorno, assim como no código principal.
"""

#praticando
print("*--*" * 10)

def sucessor_antecessor(num):
    sucessor = num + 1
    antecessor = num - 1
    return antecessor, sucessor

num = 5
antecessor, sucessor = sucessor_antecessor(num)
print("O antecessor de", num, "é", antecessor)
print("O sucessor de", num, "é", sucessor)
