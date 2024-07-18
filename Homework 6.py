my_dict = {'Петя': 1980, 'Вася': 1975, 'Стёпа': 1985}
print('Словарь: ',my_dict)
print('Год рождения Васи: ',my_dict['Вася'])
print('Год рождения Наташи: ',my_dict.get('Наташа'))
my_dict.update({'Boris': 2000, 'Jack': 2010})
del my_dict['Петя']
print(my_dict.get('Петя'))
print('Обновлённый словарь: ',my_dict)

my_set = {1, 'два', 3, 12.76, 1, 67, 3, 1}
print('Множество: ',my_set)
my_set.add(7)
my_set.add('Паровоз')
my_set.discard((67))
print('Изменённое множество: ',my_set)



