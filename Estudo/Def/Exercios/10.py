c = ('\033[m',            # 0 - sem cores 
     '\033[0;30;41m',     # 1 - vermelho
     '\033[0;30;44m',     # 2 - azul
     '\033[7;30m')        # 3 - branco invertido

def ajuda(com):
    titulo(f"Acessando o manual do comando '{com}'", 2)
    print(c[3], end='')
    help(com)
    print(c[0], end='')  # Resetar cor após help

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')

comando = ''
while True:
    titulo('Sistema de Ajuda PyHelp', 1)
    comando = input('Função ou Biblioteca -> ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo!', 1)
