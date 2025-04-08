soma = 0

for i in range(3):
  notas = float(input(f"Informe a {i+1} nota: "))
  soma+=notas
print(f"Média: {soma/3}")