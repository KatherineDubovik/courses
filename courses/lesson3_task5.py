# 5) Напишите программу. Есть 2 переменные salary и bonus.
# Salary - integer, bonus - boolean. Если bonus - true, salary
# должна быть умножена на 10. Если false - нет
# 10000, True == '$100000'
# 25000, True == '$250000'
# 10000, False == '$10000'
# 60000, False == '$60000'
salary = 5000
bonus = False
if bonus == True:
    new_salary = salary * 10
    print(f'{salary}, {bonus} == ${new_salary}')
else:
    print(f'{salary}, {bonus} == ${salary}')