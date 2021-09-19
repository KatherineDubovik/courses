'''
a = False
print('False' if a == False else 'True')

list1 = [23, 'hi', 786, 524]
list2 = [655, 10, 'hello', 54, 'bye']
print('Они равны!' if list1 == list2 else 'Good bye')

a = 'morning'
for a in range(0, 8, 2):
    print(a)
print(a)

i = 10
while i > 0:
    print(i)
    i -= 1
'''
# firstname = input ('Enter your Firstname: ')
# print(firstname)

x = '12'
if int(x) ** 2 > 1000:
    print(f'{x} == Hot')
else:
    print(f'{x} == Nope')