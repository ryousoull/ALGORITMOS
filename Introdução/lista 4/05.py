#Desenvolva um programa em que uma empresa est´a coletando informa¸c˜oes sobre a idade e o
#n´umero de horas trabalhadas de seus funcion´arios. A leitura de dados ´e realizada at´e que seja informada a idade -1. Apresente a m´edia de idade dos funcion´arios, a m´edia de horas
#trabalhadas e a idade mais alta.


idade = 0
media_idade = 0
media_horas = 0
idade_max = 0
cont  = 0 

while(idade >=0):
    idade = int(input("Informe a idade: "))
    if (idade >0):
        if (idade > idade_max):
            idade_max = idade
        horas = int(input('Informe o numero de horas trabalhadas: '))
        while(horas<0):
            horas = int(input("Informe um número de horas adquado: "))
        media_idade += idade 
        media_horas+= horas
        cont+=1




print(f"Média de idade: R$ {media_idade}")
print(f"Média de horas: {media_horas}")
print(f"Maior idade: {idade_max}")