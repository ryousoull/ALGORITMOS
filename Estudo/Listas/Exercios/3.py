exp = input('Digite a expressão: ')

lista = []

for simb in exp:
  if simb == '(':
    lista.append('(')
  elif simb == ')':
    if len(lista) > 0:
      lista.pop()
    else:
      lista.append(')')
      break
if len(lista) == 0:
  print('valido')
else:
  print('erro')