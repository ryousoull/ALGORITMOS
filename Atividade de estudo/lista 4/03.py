#Escreva um programa que permita ao usu´ario informar o pre¸co de um carro, a taxa de
#deprecia¸c˜ao mensal e o n´umero de meses. O programa deve calcular e exibir o valor do carro mˆes
#a mˆes e o valor total de deprecia¸c˜ao ao final do per´ıodo.

taxa_total = 0

preco_carro = int(input("Informe o preço do carro: "))

taxa = int(input("Informe a taxa de depresiação mensal: "))

meses = int(input("Informe o número de meses: "))

for i in range(meses):
    taxa_total += taxa
print(f'Valor final = {taxa_total + preco_carro}')