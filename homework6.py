my_dict = {'Иванов': 2001, 'Петров': 1997, 'Сидоров': 1952}
print(my_dict)

print(my_dict.get('Петров'))
print(my_dict.get('Петрова', 'Такой фамилии не найдено'))

# a = input('Введите фамилию, чтобы увидеть год рождения: ')
# print(my_dict.get(a, 'Введенная Вами фамилия не найдена в списке.'))

#my_dict['Smith'] = 1886
#my_dict['Stone'] = 2014

my_dict.update({'Smith':1986, 'Stone':2019})
print ('Словарь с двумя добавленными фамилиями: ', my_dict)

my_dict.pop('Сидоров')
print('Словарь после удаления одной пары: ', my_dict)

my_set = {1, 2, 0, 'Ivanob', True, 2, -2, 0, (4, 0, 1), 'a', 0.52}
print('Множество: ', my_set)

my_set.add(-223.26232)
my_set.add('New_element')
my_set.discard(0)

print('Множество с двумя добавленными и одним удалённым элементом: ', my_set)
