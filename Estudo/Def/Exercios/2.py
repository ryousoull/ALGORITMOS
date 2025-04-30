from time import sleep


def cont (i, f, p):
  if p <0:
    p *= -1 # p = p * -1 
  if p == 0:
    p == 1
  print('-=' * 20)
  print(f'Contagem de {i} até {f} de {p} em {p}')
  sleep(1.5)
  
  if i < f:
    c = i 
    while c <= f:
      print(f'{c} ', end='', flush=True)
      sleep(0.5)
      c += p
    print('FIM')
  else:
    c = i
    while c >= f:
      print(f'{c} ', end='', flush=True)
      sleep(0.5)
      c -= p
    print('FIM')
  
  

cont(1,10,1)
cont(10,0,2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início:  '))
fim = int(input('Fim:  '))
pas = int(input('Passo:  '))
cont(ini,fim,pas)