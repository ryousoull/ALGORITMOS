# Crie um programa que conte quantos n´umeros divis´ıveis por 3 e por 5 existem entre 1 e 200
# usando um loop for

# cont = 0

# for i in range(15,201,15):
#     cont+=1
# print(f'Quantidade de números divisíveis por 3 e 5 entre 1 e 200: {cont}')

# ou

cont = 0

for i in range(1,201):
    if i % 3 == 0 and i % 5 == 0:  
      cont += 1  
print(f'Quantidade de números divisíveis por 3 e 5 entre 1 e 200: {cont}')