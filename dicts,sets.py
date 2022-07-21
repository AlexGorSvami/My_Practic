telephone_dict = dict()
capitals_dict = {'Russia': 'Moscow', 'Ukraine': 'Kiev'}
dict_ = {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}
# ключами словарей могут быть только неизменяемые типы данных: строки, кортежи, целые числа, булевые значения и тд.
# print(capitals_dict['Russia'])
#
# for country, capital in capitals_dict.items():
#     print(country, '->', capital)
#
# capitals_dict['France'] = 'Paris'
# print(capitals_dict)


web_dict = {'title': 'Wed-рфзработчик с нуля',
        'duration': 19,
        'mentors':['Николай Лопин', 'Алёна Батицкая', 'Алексей Дацков', 'Александр Беспоясов', 'Евгений Корытов', 'Алексей Кулагин', 'Ильназ Гильязов', 'Владимир Языков', 'Владимир Чебукин', 'Эдгар Нуруллин', 'Александр Дудинский']

}
java_dict = {'title': 'Java-разработчик с нуля',
        'duration': 11,
        'mentors': ['Павел Дерендяев', 'Алексей Яковлев', 'Дмитрий Гордин', 'Сергей Сердюк', 'Анатолий Корсанов', 'Вадим Ерошевичев', 'Алексей Фомичев', 'Филлип Воронов']

}


frontend_dict = {'title':'Frontend-разработчик с нуля',
        'duration': 13,
        'mentors': ['Татьяна Тен', 'Алёна Батицкая', 'Александр Фетискин', 'Александр Беспоясов', 'Александр Шлейко', 'Денис Ежков', 'Ильназ Гильязов', 'Владимир Чебукин', 'Михаил Ларченико', 'Эдгар Нуруллин', 'Николай Лопин', 'Евгений Шек', 'Валерий Хаслер']}


# print(len(frontend_dict['mentors']))

courses_list = [web_dict, frontend_dict, java_dict]

course_id = None
max_count = 0
for id, course in enumerate(courses_list):
    # print()
    # print(course)
    mentors_count = len(course['mentors'])
    if max_count < mentors_count:
        max_count = mentors_count
        course_id = id
# print(max_count)
# print(courses_list[course_id]['title'])
# print(f"На курсе {courses_list[course_id] ['title']}, {max_count} преподователей")
# print("На курсе", courses_list[course_id]['title'], max_count, 'преподователей')
# print('На курсе {} {} преподователей'.format (courses_list[course_id]["title"], max_count))


# keys = frontend_dict.keys()
# print(type(keys), keys)
# values = frontend_dict.values()
# print(type(values), values)
#
# print()
# keys_list = list(keys)
# print(keys_list[2])
#
# values_list = list(values)
# print(values_list[2])
# print(values_list[2][3])

# if 'price' in frontend_dict.keys():
#     print(frontend_dict['price'])
# else:
#     print('Нет такого ключа price')
# if frontend_dict.get('price') is not None:
#     print(frontend_dict.get('price'))
# else:
#     print(print('Нет такого ключа price'))
#
#
# keys_list = ['title', 'duration', 'mentors', 'price']
# for key in keys_list:
#     print(frontend_dict.get(key))
#
# frontend_dict['price'] = 100000
# print(frontend_dict)
# frontend_dict['price'] = 95000
# print(frontend_dict)

# if 'price' not in frontend_dict.keys():
#     frontend_dict['price'] = 95000
# else:
#     pass
# print(frontend_dict)


frontend_dict.setdefault('price', 95000)
print(frontend_dict)


web_set = set(web_dict['mentors'])
frontend_set = set(frontend_dict['mentors'])
java_set = set(java_dict['mentors'])

print(list(web_set & frontend_set | java_set))
print(web_set & frontend_set & java_set)
print(*list(web_set & frontend_set))

web_list = web_dict['mentors']
frontend_list = frontend_dict['mentors']
java_list = java_dict['mentors']

all_list = web_list + frontend_list + java_list
print((len(all_list)), all_list)

print()

all_set = web_set | frontend_set | java_set
print(len(all_set), all_set)
# разность множеств
print(web_set - frontend_set)
print()
print(frontend_set - web_set)
# симметрическая разность множеств
print(web_set ^ frontend_set)
print()
print(frontend_set ^ web_set ^ java_set)

print(web_set.intersection(frontend_set))
print(web_set & frontend_set)

print(web_set.union(frontend_set, java_set))

print(web_set.difference(frontend_set))
print()
print(frontend_set.difference(web_set, java_set))

print(frontend_set.symmetric_difference(web_set).symmetric_difference(java_set))
