spis_el = []
kol_el = input('Введите количество элементов: ')
for i in range(int(kol_el)):
    el = int(input('Введите ' + str(i + 1) + ' эллемент: '))
    spis_el.append(el)

spis_el.sort()
print(spis_el)