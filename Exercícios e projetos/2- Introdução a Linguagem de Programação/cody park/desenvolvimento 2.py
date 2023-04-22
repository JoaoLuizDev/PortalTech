"""
Desenvolva um código que utilize as seguintes características de um veículo:
- Quantidade de rodas;
- Peso bruto em quilogramas;
- Quantidade de pessoas no veículo.

Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
- A: Veículos com duas ou três rodas;
- B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
- C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
- D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas; 
- E: Veículos com quatro rodas ou mais e com mais de 6000 kg.

*obs. Na categoria C, a informação correta é "peso maior que 3500 e até 6000kg"
"""

rodas = int(input("Qual a quantidade de rodas do veículo? "))
peso = float(input("Qual o peso bruto em quilogramas? "))
pessoas = int(input("Qual a quantidade de pessoas no veículo? "))
if rodas == 2 or rodas == 3:
  print("Sua habilitação deve ser categoria A.")
elif rodas >= 4 and pessoas <= 8 and peso <= 3500:
  print("Sua habilitação deve ser categoria B.")
elif rodas >= 4 and 3500 < peso <= 6000 and pessoas <= 8:
  print("Sua habilitação deve ser categoria C.")
elif rodas >= 4 and pessoas > 8:
  print("Sua habilitação deve ser categoria D.")
elif rodas >= 4 and peso > 6000:
  print("Sua habilitação deve ser categoria E.")
else:
  print("Veículo não pertence a nenhuma categoria listada.")
