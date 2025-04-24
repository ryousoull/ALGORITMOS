# Na matem´atica, um n´umero perfeito ´e um n´umero inteiro cuja soma de todos os seus divisores
# positivos pr´oprios (excluindo ele mesmo) ´e igual ao pr´oprio n´umero. Por exemplo: o n´umero 6 ´e perfeito, pois
# # 1+2+3 ´e igual a 6. Construa um programa que receba um n´umero inteiro e que verifique se ele ´e um n´umero
# perfeito. Caso o n´umero seja perfeito, o programa deve imprimir “´e um n´umero perfeito”. Caso contr´ario, a
# mensagem “n˜ao ´e um n´umero perfeito” deve ser impressa.

soma_divisor = 0

numberPerfect = int(input("informe um número: "))

for i in range(1,numberPerfect):
  if (numberPerfect % i == 0):
    soma_divisor+=i
    
if (soma_divisor == numberPerfect):
  print('Número perfeito')
else:
  print("Não é perfeito")