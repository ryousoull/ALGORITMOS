cigarrets = int(input("Informe a quantidade de cigarros usados por dia: "))
cigarretsYear = int(input("Por quantos anos fumou essa quantidade de cigarros: "))
print(f"Tempo total de vida perdido foi de {(cigarrets*cigarretsYear*360*10)/ 1440} dias")