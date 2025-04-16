numeros_extenso = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quartoze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

n = int(input('Informe um número entre 0-20: '))

while not(0 < n <=20):
  n = int(input('Informe um número entre 0-20 corretamente: '))

print(f' número digitado: {numeros_extenso[n]}')
  