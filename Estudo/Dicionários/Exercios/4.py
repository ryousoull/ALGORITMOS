pessoas = []
pessoa = {}

while True:
  pessoa ['nome'] = str(input('Nome: '))
  sex = str(input('Sexo: [M/F] '))
  while not (sex in 'MmFf'):
    print('ERRO! Por favor, digite apenas M ou F.')
    sex = str(input('Sexo: [M/F] '))
  pessoa['sexo'] = sex
  pessoa ['idade'] = int(input('Idade: '))
  r = str(input('Quer continuar?  [S/N] '))
  while not (r in 'SsNn'):
    print('ERRO! Por favor, digite apenas S ou N.')
    r = str(input('Quer continuar?  [S/N] '))
  pessoas.append(pessoa.copy())
  if r in 'Nn':
    break
print('-=' * 30)
print(pessoas)
media = sum(p['idade'] for p in pessoas) / len(pessoas)
print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for i, c in enumerate(pessoas):
  if c['sexo'] in 'Ff':
    print(f'{c['nome']} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in pessoas:
  if p['idade'] >= media:
    print('  ', end='')
    for k, v in p.items():
      print(f'{k} = {v}; ', end='')
    print()
print('----->> ENCERRADO <<-----')