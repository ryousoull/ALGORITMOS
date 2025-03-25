usuario = input("Informe o usuário: ")


while (not (5 <= len(usuario) <= 15) or not usuario.islower() or (usuario[0] == '_' or usuario[-1] == '_') or '__' in usuario):
    usuario = input("Informe um nome de usuário válido: ")

print(f'Bem-vindo {usuario}')
