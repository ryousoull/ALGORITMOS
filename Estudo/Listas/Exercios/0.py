lista = []

for i in range(5):
  lista.append(int(input('Informe o valor: ')))
  
print('-='*35)

print(f' Você digitou os valores {lista}')

for c,i in enumerate(lista):
  if i == max(lista):
    print(f'O maior valor digitado foi {i} na posiçao {c}')
  elif i == min(lista):
    print(f'O menor valor digitado foi {i} na posiçao {c}')

print('-='*35)
