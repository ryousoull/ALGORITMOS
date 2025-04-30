def maiorNumero(*num):
  print('~' * 35)
  print("Analisando os valores passados...")
  tam = len(num)
  for i in num:
    print(f'{i} ', end="")
  print(f'foram informados {tam} valores ao todo')
  print(f'O maior valor informado foi {max(num)}.')
  print('~' * 35)
  
    


maiorNumero(2,9,4,5,7,1)