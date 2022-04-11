def unik(razd):
  z=vvod.split(razd)
  h=[]
  for i in range(len(z)):
    if z.count(z[i])==1:
      h.append(z[i])
  print('Результат: ',', '.join(h))
vvod=(input('Введите элементы списка через запятую ') )
if (vvod.count(',')>=1 and vvod.count(';')>=1) or (vvod.count(',')>=1 and vvod.count('/')>=1) or (vvod.count(';')>=1 and vvod.count('/')>=1):
  print('Не допустимый ввод')
elif vvod.count(',')>=1:
  unik(',')
elif vvod.count(';')>=1:
  unik(';')
elif vvod.count('/')>=1:
  unik('/')
