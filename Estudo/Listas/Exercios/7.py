matriz = [
  [0,0,0], [0,0,0], [0,0,0]
]

soma_par = maior = soma_col = 0

for l in range(3):
  for c in range(3):
    matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
    
print('-=' * 30)

for l in range(3):
  for c in range(3):
    print(f' [{matriz[l][c]:^5}]', end='')
    if matriz[l][c] % 2 == 0:
      soma_par += matriz[l][c]
  print()

print('-=' * 30)

print(f' Soma dos vaolores pares: {soma_par}')

for l in range(3):
  soma_col += matriz[l][2]
print(f' Soma dos valores da terceira coluna: {soma_col}')

for c in range(3):
  if c == 0 or matriz[1][c] > maior:
    maior = matriz[1][c]
print(f' O mair elemento da segunda linha: {maior}')
