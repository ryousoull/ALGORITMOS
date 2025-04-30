
import random as rd

n1 = rd.randint(1,10)
n2 = rd.randint(1,10)
n3 = rd.randint(1,10)
n4 = rd.randint(1,10)
n5 = rd.randint(1,10)

valores = [n1,n2,n3,n4,n5]

print(f'Sorteando 5 valores da lista: ',end="")
for i in valores:
  print(f'{i} ', end="")
print('Pronto!')


def somaPar(lst):
  sum = 0
  print(f'Somando os valores pares de {lst}, temos ', end="")
  for i in lst:
    if i % 2 == 0:
      sum+=i
  print(sum)
  
somaPar(valores)
