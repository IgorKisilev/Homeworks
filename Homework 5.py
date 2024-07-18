immutable_var = 'строка', 1.67, True, 5
print(immutable_var)
#immutable_var[0] = 98
#print(immutable_var)
#Кортеж относится к неизменяемым типам данных, не поддерживает обращение по элементам


mutable_list = [1, 4.5, 'second', 'h', False ]
print('Immutable tuple: ', mutable_list)
mutable_list.append('Modified')
print('Mutable list: ', mutable_list)
mutable_list[1] = True
print('Mutable list: ', mutable_list)
mutable_list.extend('Dog')
print('Mutable list: ', mutable_list)
mutable_list.remove(1)
print('Mutable list: ', mutable_list)


