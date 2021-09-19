# 6)Проверить, все ли элементы одинаковые,пример;
# [1, 1, 1] == True
# [1, 2, 1] == False
# ['a', 'a', 'a'] == True
list1 = [2, 1, 1]
if len(set(list1)) == 1:
    print(f'{list1} == True')
else:
    print(f'{list1} == False')