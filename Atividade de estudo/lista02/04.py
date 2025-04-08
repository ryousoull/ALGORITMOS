# Vocˆe construir´a um programa que receba 2 n´umeros. O primeiro representar´a a quantidade de
# n´umeros que ser˜ao somados e indicar´a se os n´umeros ser˜ao pares ou os ´ımpares. J´a o segundo, representar´a o
# primeiro termo da sequˆencia que ser´a somada. O seu programa deve verificar se o primeiro termo ´e par ou ´ımpar
# para, ent˜ao, realizar a soma corretamente. Se o primeiro termo for par, o programa soma os n´umeros pares; se o
# primeiro termo for ´ımpar, a soma ser´a dos n´umeros ´ımpares. Ao final, imprima apenas o resultado da soma.
# • Exemplo 1: para a entrada 4 e 5, o programa somar´a 4 termos pares a partir do n´umero 5, portanto, a soma
# ser´a 6+8+10+12;
# • Exemplo 2: para a entrada 5 e 11, o programa somar´a 5 termos ´ımpares a partir do n´umero 11, portanto, a
# soma ser´a 11+13+15+17+19.

soma= 0


quantidade = int(input("Informe a quantidade: "))
number = int(input("Informe o numero que vai começar: "))

for i in range(quantidade):
  soma+=number
  number+=2

print(soma)