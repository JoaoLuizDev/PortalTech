"""
Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e 
o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.
"""

def calculadora(numero1, numero2, operacao):

  if operacao == 1: 
    return numero1 + numero2
  elif operacao == 2:
    return numero1 - numero2
  elif operacao == 3: 
    return numero1 * numero2
  elif operacao == 4:
    if numero2 == 0:
      return "ERRO- Nenhum número pode ser dividido por zero."
    else: 
      return numero1 / numero2
  else:
    return "Operação não encontrada."

print("Esta calculadora realiza as seguintes operações:\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão")
operacao = int(input("Digite o número da operação que você deseja fazer: "))
numero1 = float(input("Digite o primeiro termo: "))
print(f"{numero1} {'+' if operacao == 1 else '-' if operacao == 2 else '*' if operacao == 3 else '/'}")
numero2 = float(input("Digite o segundo termo: "))
print(f"{numero1} {'+' if operacao == 1 else '-' if operacao == 2 else '*' if operacao == 3 else '/'} {numero2}")
resultado = calculadora(numero1, numero2, operacao)
print(f"{numero1} {'+' if operacao == 1 else '-' if operacao == 2 else '*' if operacao == 3 else '/'} {numero2} = {resultado}")
print(f"O resultado é: {resultado}")
