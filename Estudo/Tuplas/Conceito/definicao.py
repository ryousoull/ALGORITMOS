lanche = ('Suco', 'Pizza', 'Pudim')

print(lanche)

print(lanche[-1])

print(lanche[0:])

print(len(lanche))


print('='*35)

for c in lanche:
  print(f' vou comer {c}')
  
print('='*35)

for cont in range(len(lanche)):
  print(lanche[cont])
  
  
print('='*35)

for pos, comida in enumerate(lanche):
  print(f' Eu vou comer {comida} na posição {pos}')

print('='*35)

a = (2,5,4)
b = (5,8,1,2)

c = b + a
print(c)
print(c.index(4))
del(c)