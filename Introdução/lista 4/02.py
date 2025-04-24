# Crie um programa que calcule a soma dos n´umeros pares de 1 a 100 usando um loop for.


soma  = 0

for i in range(1,101):
    if(i % 2 == 0):
        soma+=i
print(f'Soma = {soma}')