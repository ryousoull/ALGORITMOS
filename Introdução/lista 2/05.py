# O desafio proposto consiste em criar um programa que receba duas notas v´alidas, entre 0.0 e
# 10.0, do usu´ario. Se uma nota inv´alida for inserida, o programa deve exibir a mensagem “Nota com valor
# inv´alido!” e solicitar uma nova entrada. Esse processo de valida¸c˜ao deve ser repetido at´e que duas notas v´alidas
# sejam fornecidas. Ap´os receber as duas notas v´alidas, o programa deve calcular a m´edia aritm´etica e exibi-la.


nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))

while( not (nota1>= 0 and nota1<=10.0 ) and not (nota2>= 0 and nota1<=10.0 )):
  print("Informe novamente as 2 notas: ")
  nota1 = float(input("Informe a nota 1: "))
  nota2 = float(input("Informe a nota 2: "))
print(f'Média das notas: {(nota2+nota1)/2}')