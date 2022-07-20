telephone_dict = dict()
capitals_dict = {'Russia': 'Moscow', 'Ukraine': 'Kiev'}
dict_ = {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}
# ключами словарей могут быть только неизменяемые типы данных: строки, кортежи, целые числа, булевые значения и тд.
print(capitals_dict['Russia'])

for country, capital in capitals_dict.items():
    print(country, '->', capital)

capitals_dict['France'] = 'Paris'
print(capitals_dict)




