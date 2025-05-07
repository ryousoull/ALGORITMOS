def ficha(jog='<desconhecido>', g=0):
  print(f'O jogador {jog} fez {g} gol(s)')
  
jogador = input('Qual o nome do jogador? ')
gols = input('Quantos gols ele fez? ')

if gols.isnumeric():
  gols = int(gols)
else:
  gols = 0

if jogador.strip() == "":
  ficha(g=gols)
else:
  ficha(jogador, gols)
  
