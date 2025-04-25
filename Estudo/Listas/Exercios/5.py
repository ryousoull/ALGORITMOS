num = [ [], []]


for i in range(7):
  n = int(input('Informe um valor: '))
  if n % 2 == 0:
    num[0].append(n)
  else:
    num[1].append(n)

print('-=' * 30)

print(num)
print(f' Os números pares digitados foram: {num[0]}')
print(f' Os números ímpares digitados foram: {num[1]}')