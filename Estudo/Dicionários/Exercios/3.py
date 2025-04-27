jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quatas patidas {jogador["nome"]} jogou? '))
total_gol = 0
for i in range(tot):
  partidas.append(int(input(f'  Quantos gols na partida {i+1}? ')))
jogador['gols'] = partidas[:]
jogador['total de gols'] = sum(partidas)
print('-' * 30)
print(jogador)
print('-' * 30)
for k, v in jogador.items():
  print(f'O campo {k} tem o valor {v}')
print('-' * 30)
print(f'O jogador {jogador['nome']} jogou {tot} partidas.')
for i, c in enumerate(jogador['gols']):
  print(f'  => Na partida {i+1}, fez {c} gols.')
print(f'Foi um total de {sum(partidas)}')
