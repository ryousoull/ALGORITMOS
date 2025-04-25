alunos = list()

while True:
  nome = input('Informe o nome do estudante: ')
  nota1 = float(input('Informe a nota1: '))
  nota2 = float(input('Informe a nota2: '))
  media = (nota1 + nota2) / 2
  alunos.append([nome, [nota1, nota2], media])
  r = input('Quer continuar [S/N]: ')
  if r in 'Nn':
    break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('=' * 26)
for i, a  in enumerate(alunos):
  print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
  
while True:
  print('-' * 30)
  opc = int(input('Informe o valor do estudante para ver suas notas [999 para encerrar]: '))
  if opc == 999:
    print('Finalizado..')
    break
  if opc <= len(alunos) -1:
    print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}')
    
print('<<<< VOLTE SEMPRE >>>>')
