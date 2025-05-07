def leiaInt(msg):
  valor = 0
  ok = False
  while ok == False:
    n = str(input(msg))
    if n.isnumeric():
      valor = int(n)
      ok = True
    else:
      print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
  return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')