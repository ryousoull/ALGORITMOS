import random as rd

n1 = rd.randint(0,10)
n2 = rd.randint(0,10)
n4 = rd.randint(0,10)
n3 = rd.randint(0,10)
n5 = rd.randint(0,10)

numeros_sorteados = (n1,n2,n3,n4,n5)
print(f' Números sorteadods: {numeros_sorteados}')

print('='*30)

print(f' Maior  número: {max(numeros_sorteados)}')
print(f' Menor número: {min(numeros_sorteados)}')


