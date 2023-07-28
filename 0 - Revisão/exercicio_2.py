"""
2-) Crie um programa que receba o valor de um produto e um cupom de desconto. O programa deve calcular o valor final com 
o desconto aplicado e exibir na tela. 
"""

valor = float(input("Digite o valor do produto em R$: "))
desconto = float(input("Digite o percentual de desconto em %: "))

valor_final = valor - ((valor / 100) * desconto)
print(f"Com um desconto de {desconto:.2f}%, o valor final será de R$ {valor_final:.2f}.")
