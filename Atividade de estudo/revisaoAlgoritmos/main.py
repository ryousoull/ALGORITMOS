maior = 0

for i in range(3):
  num = int(input("Informe o numero: "))
  

  if num > maior:
    maior = num

print(f'O maior número digitado foi: {maior}')