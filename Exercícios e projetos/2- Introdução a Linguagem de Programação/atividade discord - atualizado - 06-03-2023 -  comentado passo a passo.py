"""
Código elaborado a partir da atividade que pode ser acessada no link abaixo:
https://github.com/JoaoLuizDev/PortalTech/blob/main/Introdu%C3%A7%C3%A3o%20a%20Linguagem%20de%20Programa%C3%A7%C3%A3o/atividade%20discord%20-%2006-03-2023.png

Nese código, comentarei cada etapa, porque decidi construir o código assim e qual o objetivo esperado.

Sobre a tarefa:
Entendi que deveria ser construído um programa no qual o clienta da academia registra os nomes dos exercícios e a qauntidade de séries que ele fará no dia.
Com esse registro, o cliente poderia imprimir seu "roteiro" de exercícios, para ter um controle maior e não esquecer se já fez algum exercício,
ou ainda se fez todas as séries.
Minha ideia foi criar uma tabela. Nela, teremos nome do exercício, número de séries, e se o exercício já foi realizado.

Saída esperada:
Tipo de exercício     série       Realizado
Braço                 1
                      2
                      3

Na coluna "Realizado", o cliente poderia marcar que terminou a série e assim controlar sua rotina.
"""

# Criei uma função chamada "imprimir_serie" para que o cliente da academia faça seu roteiro de exercício e possa imprimir 
def imprimir_serie():
    # Solicita o nome do cliente e a quantos tipos deiferentes de exercícios ele quer fazer
    nome = input("Digite seu nome: ")
    num_exercicios = int(input("Quantos tipos de exercícios você quer fazer hoje? "))
    exercicios = []
    # O programa pergunta ao cliente o nome de cada exercícios e a quantidade de séries. É criada uma lista de exercícios.
    for i in range(num_exercicios):
        nome_exercicio = input(f"Qual é o nome do {i+1}º exercício? ")
        vezes_exercicio = int(input(f"Quantas séries você quer fazer o exercício {nome_exercicio}? "))
        exercicios.append((i+1, nome_exercicio, vezes_exercicio))
    # Aqui estou editando a tabela que mostrará a lista de exercícios.
    print("")
    print(f"Roteiro de exercícios do(a) {nome}")
    print("Tipo\tExercício\tRealizado")
    # Para cada tipo de exercício, será impresso o exercicio  imprime o exercício e quantas vezes ele deve ser realizado
    for exercicio in exercicios:
        for i in range(exercicio[2]):
            # Se for a primeira série do exercício, imprime o tipo e nome do exercício
            if i == 0:
                print(f"{exercicio[0]}\t{exercicio[1]}\t")
            # Se não for a primeira série do exercício, imprime apenas o nome do exercício
            else:
                print(f"\t{exercicio[1]}\t")

# Mensagem da academia ao cliente
print("Academia Perde Apança. Seja bem-vindo.")
# Usuário pode escolher se quer cosntruir e imprimir seu roteiro de exercício
imprimir = input("Vamos imprimir sua série de exercícios? Digite 'sim' para imprimir, ou 'não' para sair. ").strip().lower()
print("")

# 'sim' para construir e imprimir ou 'não' para sair e treinar sem o roteiro 
while imprimir != "sim" and imprimir != "não":
    imprimir = input("Opção inválida. Digite 'sim' para imprimir, ou 'não' para sair. ").strip().lower()

# se a resposta for 'sim', começa a função "imprimir_serie" 
if imprimir == "sim":
    imprimir_serie()
# se a resposta for'não', deseja bom treino ao cliente.
if imprimir == "não":
    print("Ok, bom treino. Qualquer dúvida, só chamar o professor.")

# Ao final, uma propaganda da academia e uma brincadeira com o cliente
print("")
print("Caso esteja cansado de exercícios e queira resultado rápido, chame nosso especialista, professor Akiso Tomobomba.")
print("Academia Perde Apança agradece sua preferência.")


"""
Alguns comentários:
começar com função - embora não seja uma regra declarar funções no início de um arquivo Python, 
                     é uma boa prática fazê-lo para evitar erros e tornar o código mais organizado.

.lower() - método que pode ser aplicado a uma string, para transformar todas as letras em minúsculas.
           Isso é importante para evitar erro caso o cliente digite, por exemplo, "sim" e o programa só aceite "Sim", com letra inicial maiúscula.

.strip() - método que retorna uma cópia da string original, com os espaços em branco no início e no final removidos. 
           Importante: não altera a string original. Isso evita erro caso o cliente digite, por exemplo, " sim", "sim ".
"""
