immutable_var = 1, 'Pavel', 5, -0.6, False, [2, 5, 90]
print('Tuple (Кортеж): ', immutable_var)

mutable_list = [1, 'Pavel', 5, -0.6, False, [2, 5, 90]]
print('List (Список): ', mutable_list)
a = input('Введите значение нового элемента списка: ')
mutable_list.append(a)
print('Обновлённый список: ', mutable_list)
