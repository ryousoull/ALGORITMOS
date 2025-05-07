def notas(*num,sit=False):
  
  dicionario = dict()
    
  media = sum(num) / len(num)
    
  dicionario['total'] = len(num)
  dicionario['maior'] = max(num)
  dicionario['menor'] = min(num)
  dicionario['média'] = media
  
  if (sit == True):
    if (media >= 7):
      dicionario['situação'] = 'BOA'
    else:
      dicionario['situação'] = 'Ruim'
    
  return dicionario

  
      
print(notas(5,5))