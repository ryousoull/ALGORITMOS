palavras_aleatorias = (
    "girassol",
    "montanha",
    "abacaxi",
    "relâmpago",
    "tartaruga",
    "universo",
    "luz",
    "mistério",
    "vento",
    "tempo"
)

for p in palavras_aleatorias:
  print(f' \n Na palavra {p.upper()} temos:  ', end='')
  for vogal in p: 
    if vogal.lower() in 'aeiou':
      print(vogal, end=' ')