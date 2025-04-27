jogadores = []
jogador = {}


while True:
  partidas = []
  jogador['nome'] = input('Nome do jogador: ')
  tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
  for i in range(tot):
    partidas.append(int(input(f'  Quantos gols na partida {i+1}? ')))
  jogador['gols'] = partidas[:]
  jogador['total'] = sum(partidas)
  r = input('Quer continuar? [S/N] ')
  jogadores.append(jogador.copy())
  if r in 'Nn':
    break
print('-=' * 20)
print(f'{"cod":<4}{"nome":<10}{"gols":<15}{"total":>5}')
print('-'*35)
for i, j in enumerate(jogadores):
  print(f'{i:<4}{j["nome"]:<10}{str(j["gols"]):<15}{j["total"]:>5}')
print('-'*35)
while True:
  opc = int(input("Mostrar dados de qual jogador? (999 para parar) "))
  if opc == 999:
    break
  if 0 <= opc < len(jogadores):
    print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[opc]["nome"]}:')
    for i, j in enumerate(jogadores[opc]['gols']):
      print(f' No jogo {i+1} fez {j} gols.')
  print('-'*35)

    
  