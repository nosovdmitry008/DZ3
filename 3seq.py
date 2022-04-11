vvod1=(input('Введите элементы 1-го списка: ') )
vvod2=(input('Введите элементы 2-го списка: ') )
z1=vvod1.split(',')
z2=vvod2.split(',')
h=[]
for i in z2:
  if z1.count(i)>0:
    for h in range(z1.count(i)):
      z1.remove(i)
print('Результат: ',', '.join(z1))
