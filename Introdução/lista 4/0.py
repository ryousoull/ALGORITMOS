#4. Escreva um programa que calcule a m´edia dos n´umeros de 1 a 100 usando um loop for.

soma = 0

for i in range(1,101):
    soma+=i
print(f'média = {soma/100}')   