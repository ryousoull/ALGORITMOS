 #Se uma tartaruga est´a subindo um poste de 2 metros de altura e some 1 metro a cada dia, mas a cada noite ela escorrega e desce 0.5 metros, em quantos dias ela chegar´a ao topo? 
 
percurso = 0
poste = 2
desce = 0.5
dias = 0

while (percurso < poste):
  percurso+= 1
  if (percurso < poste):
    percurso-= desce
  dias+=1
print(dias)
