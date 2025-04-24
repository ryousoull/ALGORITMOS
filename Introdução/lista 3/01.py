tamanho = int(input("Informe o tamanho da pirâmide: "))

for i in range(1,tamanho+1):
  print(' '*(tamanho-i) + '*' * (2 * i - 1))
  
# # inversa

for i in range(tamanho, 0, -1):
    print(' ' * (tamanho - i) + '*' * (2 * i - 1))
