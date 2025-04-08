matriz = [ [0,0,0,0] , [0,0,0,0] , [0,0,0,0] , [0,0,0,0] ]
sumBody = 0

for i in range(0,3):
  sum1 = 0
  for j in range(0,4):
    matriz [i][j] = int(input(f"Informe a nota {j+1} do aluno {i+1}: "))
    sum1 += matriz[i][j]
  media = sum1 / 4
  print(f" Média: {media}")
  sumBody += media
  mediaBody = sumBody / 3 
print(f'Média da turma: {mediaBody}')
print(matriz)