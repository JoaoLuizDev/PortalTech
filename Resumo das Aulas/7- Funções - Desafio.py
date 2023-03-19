"""
João precisa calcular seu Índice de Massa Corporal (IMC) para avaliar seu peso ideal. Sabendo que a fórmula para
calcular o IMC é: peso ÷ altura², crie um programa que calcule e informe a classificação do IMC.
"""

# calcular índice do IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

resultado = calcular_imc(85, 1.85)
print(f"O IMC é de {resultado:.2f}.")
     
print("*-" * 10

# calcular classificação do IMC
def calculadoraImc(peso, altura):
    imc = peso / (altura * altura)
    if (imc <= 18.5): return "Magreza"
    elif (imc > 18.5) and (imc <= 24.9): return "Saudavel"
    elif (imc >= 25) and (imc <= 29.9): return "Sobrepeso"
    elif (imc > 30) and (imc <= 34.9): return "Obesidade grau 1"
    elif (imc > 35) and (imc <= 39.9): return "Obesidade severa grau 2"
    else : return "Obesidade morbida grau 3"

resultado = calculadoraImc(92, 1.78)
print(f"\nDe acordo com o cálculo do IMC, o resultado foi de", resultado)
      
print("*-" * 10

# calcular índice e classificação do IMC

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if (imc <= 18.5): 
        classificacao = "Magreza"
    elif (imc > 18.5) and (imc <= 24.9): 
        classificacao = "Saudável"
    elif (imc >= 25) and (imc <= 29.9): 
        classificacao = "Sobrepeso"
    elif (imc > 30) and (imc <= 34.9): 
        classificacao = "Obesidade grau 1"
    elif (imc > 35) and (imc <= 39.9): 
        classificacao = "Obesidade severa grau 2"
    else: 
        classificacao = "Obesidade morbida grau 3"
    return imc, classificacao

indice_imc, classificacao_imc = calcular_imc(85, 1.85)
print(f"O IMC é de {indice_imc:.2f}, e a classificação é {classificacao_imc}.")



