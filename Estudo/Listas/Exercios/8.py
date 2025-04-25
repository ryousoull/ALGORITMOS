import random as rd
import time as tm

lista = list()
jogos = list()

print('-=' * 30)
print('    JOGA NA MEGA SENA    ')
print('-=' * 30)

quant = int(input('Informe quantos jogos voê quer: '))
tot = 1

while tot <= quant:  
  cont = 0
  while True:
    num = rd.randint(1,60)
    if num not in lista:
      lista.append(num)
      cont+=1
    if cont >= 6:
      break
  lista.sort()  
  jogos.append(lista[:])
  lista.clear()
  tot+=1
  
print('-=' * 30)

for i in range(len(jogos)):
  print(f'Jogo {i+1}: {jogos[i]}')
  tm.sleep(1)
print('-=' * 5 , '< BOA SORTE >', '-=' * 5)
