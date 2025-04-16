listagem = ('Lápis', 1.99, 
            'Borracha', 8, 
            'Mochila', 50.99,
            'Estojo', 20.99)

print('-'*40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-'*40)

for i in range(len(listagem)):
  if i % 2 == 0:
    print(f' {listagem[i]:.<30}', end='')
  else:
    print(f' RS{listagem[i]:>7.2f}')
print('-'*40)
