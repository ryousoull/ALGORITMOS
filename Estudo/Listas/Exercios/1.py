numeros = []

valor = int(input('Informe o valor: '))
print('Adicionado com sucesso!')
numeros.append(valor)

continuar = input("Quer continuar?  [S/N]").upper()

while (continuar == 'S'):
  valor = int(input('Informe o valor: '))
  if valor in numeros:
    print('Não será adicionado devido a duplicação de valores.')
  else: 
    print('Adicionado com sucesso!')
    numeros.append(valor)
  continuar = input("Quer continuar?  [S/N] ").upper()

print('-='*35)

numeros.sort()

print(f'números digitados: {numeros}')  
  

