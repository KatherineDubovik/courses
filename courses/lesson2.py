# 1. Создать произвольный словарь
dict_n = {'one': 32, 98: 1, 123: 'test'}
print(dict_n)
# 2. Добавить новый элемент с ключом типа str и значением типа int
dict_n['new'] = 56
print(dict_n)
# 3. Добавить новый элемент с ключом типа кортеж(tuple) и значением типа список(list)
key_t = (45, 2, 19)
value_l = [63, 'list', 1]
dict_n[key_t] = value_l
print(dict_n)
# 4. Получить элемент по ключу
print(dict_n[98])
# 5. Удалить элемент по ключу
del dict_n['one']
print(dict_n)
# 6. Получить список ключей словаря
print(dict_n.keys())
