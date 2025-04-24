# maior = 0

# num = int(input(" Digite o numero: "))

# while (num!=0):
#   maior = num
#   num = int(input("Infome o numero: "))
  
# print(f'o maior numero digitado é: {maior}')

#ou 

listaNumeros = []

num = int(input(" Digite um numero:  [0 para sair]"))

while (num!=0):
  listaNumeros.append(num)
  num = int(input("Infome o numero: "))
  
print(f'o maior numero digitado é: {max(listaNumeros)}')
