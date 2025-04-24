palavra = str(input("Informe uma palavra: "))
if palavra==palavra[::-1]:
    print("É palindromo")

palavra = str(input("Informe uma palavra: "))
tamanho = len(palavra)
for i in range(tamanho):
    tamanho -= 1
    if(palavra[i]==palavra[tamanho]):
        print(True)
    else:
        print(False)