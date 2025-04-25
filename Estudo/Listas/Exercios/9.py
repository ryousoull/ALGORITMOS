zumbis = []
caidos = 0
maior = 0
nome_maior =''

while True:
    nome = input('Informe o nome do zumbi: [GAME OVER para encerrar] ')
    if nome == 'GAME OVER':
        break
    hr = int(input('Informe a quantidade de horas caminhadas: '))
    
    if hr < 10:
        print(f'{nome} ainda está de pé!')
    else:
        print(f'{nome} perdeu o evento..')
        caidos += 1
        if hr > maior:
          maior = hr
          nome_maior = nome

    zumbis.append([nome, hr])

print(f'\nTotal de zumbis: {len(zumbis)}')
print(f'Zumbis caídos: {caidos}')
print(f'O zumbi mais resistente foi {nome_maior}, que andou {maior} horas ')
