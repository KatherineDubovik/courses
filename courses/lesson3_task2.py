# 2)Если х в квадрате больше 1000 - пишем "Hot" иначе - "Nope"
# '50' == "Hot"
# 4 == "Nope"
# "12" == "Nope"
# 60 == "Hot"
x = 50
if x ** 2 > 1000:
    print(f'{x} == Hot')
else:
    print(f'{x} == Nope')