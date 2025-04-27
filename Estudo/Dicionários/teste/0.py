# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# pessoas['peso'] = 90.0
# for k, v in pessoas.items():
#   print(f' {k} = {v}')


# brasil = []
# estado = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = { 'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado.copy())
# brasil.append(estado2.copy())

# print(brasil)
# print(brasil[1].keys())

estado = dict()
brasil = list()

for c in range(3):
  estado['uf'] = input('Informe a Unidade Federativa: ')
  estado['sigla'] = input('Informe a Sigla do Estado: ')
  brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for v in e.values():
      print(v, end=' ')
    print()