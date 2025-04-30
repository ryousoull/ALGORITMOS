import random as rd
import time as tm
import operator as op
dado = {
  'jogador1': rd.randint(1,6), 
  'jogador2': rd.randint(1,6),
  'jogador3': rd.randint(1,6), 
  'jogador4': rd.randint(1,6)
}


ranking = {}

print('Valores Sorteados')

for k, v in dado.items():
  print(f'O {k} tirou o valor {v}')
  tm.sleep(1)

print('-' * 27)
ranking = sorted(dado.items(), key=op.itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
  print(f' {i+1} lugar: {v} com {v}')
  tm.sleep(1)

