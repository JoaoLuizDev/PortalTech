"""
Problema: Desenvolva um programa que só deve aceitar números pares. Siga as seguintes instruções:

- caso um número ímpar seja digitado, informe ao usuário que ele digitou um valor ímpar e peça novamente por um número par;
- caso uma letra seja digitada, informe ao usuário que ele digitou um caractere inválido e peça novamente por um número par.
"""

numeroCorreto = False                                                 # consideramos que a condição inicial seja falsa
while (numeroCorreto == False):                                       # código deverá repetir enquanto essa condição se repetir
   print("Insira um número par")
   try:
       numero = int(input())
       if (numero%2 == 0):                                            # testa o resto da divisão. Ex: 7 % 2. O número 2 "cabe" 3 vezes no 7 e sobra 1, logo número ímpar.
           numeroCorreto = True                                       # se o resto da divisão for 0, é par, logo, condição True. 
           print("Você digitou um numero par !")                      # Ex. 10 % 2. O número 2 "cabe" 5 vezes no 10 sem resto de divisão.
       else :
           print("Você digitou um número impar")                      # programa informa se o número for ímpar.
   except:
       print("Caracter inválido, por favor digite um número par")     # informa que o caracter digitado não é aceito
