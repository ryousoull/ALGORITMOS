#. Crie um programa que pergunte ao usu´ario o valor inicial de um dep´osito em uma conta
#poupan¸ca, a taxa de juros anual e o n´umero de anos. O programa deve calcular e exibir o valor
#do dep´osito mˆes a mˆes e o valor total ganho com juros no per´ıodo.



deposito = int(input("Informe o valor do depósito inicial: "))
taxa = int(input("Informe a taxa de juros anual: [ex: 10%] ")) /100 /12
anos = int(input("Informe o número de anos: "))

valor_total_ganho = deposito

for i in range(anos*12):
    valor_total_ganho += valor_total_ganho * taxa
    print(f'{valor_total_ganho}')
print('-------------------------------')
print(valor_total_ganho - deposito)