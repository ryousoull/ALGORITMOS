#7. Crie um programa que gere a sequˆencia de Fibonacci at´e o d´ecimo termo usando um loop for.

termo1 = 1
termo2 = 1
termo = int(input('insira o termo que você deseja da sequência de fibonacci: '))
print(termo1)
print(termo2)
for i in range(1, termo-1, 1):
  prox_termo = termo1+termo2 
  print(prox_termo) #
  termo1 = termo2 
  termo2 = prox_termo 