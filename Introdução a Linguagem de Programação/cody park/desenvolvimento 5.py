"""
Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário 
escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” 
e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o 
resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 
"""

def calculadora():
    while True:
        print("Esta calculadora realiza as seguintes operações:\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n0. Sair")

        operacao = input("Digite o número da operação que você deseja fazer: ")
        
        if operacao == "0":
            print("Encerrando a calculadora...")
            break
        elif operacao in ("1", "2", "3", "4"):
            operacao = int(operacao)
            numero1 = float(input("Digite o primeiro termo: "))
            print(f"{numero1} {'+' if operacao == 1 else '-' if operacao == 2 else '*' if operacao == 3 else '/'}")
            numero2 = float(input("Digite o segundo termo: "))
            print(f"{numero1} {'+' if operacao == 1 else '-' if operacao == 2 else '*' if operacao == 3 else '/'} {numero2}")

            if operacao == 1:
                resultado = numero1 + numero2
            elif operacao == 2:
                resultado = numero1 - numero2
            elif operacao == 3:
                resultado = numero1 * numero2
            elif operacao == 4:
                if numero2 == 0:
                    resultado = "ERRO - Nenhum número pode ser dividido por zero."
                else:
                    resultado = numero1 / numero2

            print(f"{numero1} {'+' if operacao == 1 else '-' if operacao == 2 else '*' if operacao == 3 else '/'} {numero2} = {resultado}")
            print(f"O resultado é: {resultado}")
            print("-*#" * 16)
        else:
            print("Opção não encontrada.")
            print("-*#" * 16)
            continue

calculadora()
