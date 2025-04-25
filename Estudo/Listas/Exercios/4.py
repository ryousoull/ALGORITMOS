pessoas = []
maior = menor = 0

while True:  
    dados = []
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    
    pessoas.append(dados[:])
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if r != 'S':
        break

print('-=' * 30)
print(f'Você cadastrou ao todo {len(pessoas)} pessoas.')

print(f"O maior peso foi de {maior}Kg. Peso de ", end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()

print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
