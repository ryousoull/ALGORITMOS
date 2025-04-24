# Crie um programa que pergunte a popula¸c˜ao inicial e a taxa de crescimento populacional de
#uma cidade. Exiba a popula¸c˜ao mˆes a mˆes para os 60 primeiros meses. Calcule a popula¸c˜ao
#total ao final do per´ıodo.

populacao = int(input('Informe a população: '))
taxa = int(input("Informe a taxa de crescimento: [ex: 10% ou 20%]"))

for i in range(60):
    populacao+= populacao* (taxa/100)
    print(f'População no mês {i+1}: {populacao}')