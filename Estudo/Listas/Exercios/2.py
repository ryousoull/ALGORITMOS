numeros = []

for c in range (5):
  n = int(input('Informe um valor: '))
  if c == 0 or n > numeros[-1] :
    numeros.append(n)
    print('adicionado ao final da lista..')
  else:
    pos = 0
    while pos < len(numeros):
      if n <= numeros[pos]:
        numeros.insert(pos, n)
        print(f'adicionado na posição {pos} da lista')
        break
      pos+=1
      
print('-='*35)

print(numeros)