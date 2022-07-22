# def square(number):
#     result = number ** 2
#     return result
#
# print(square(5))

# def square(number):
#     """
#     this is my first function
#     """
#     result = number ** 2
#     print(result)
#
#
# res = square(5)
# print(res)
#
# help(square)


# def square_2():
#     number = int(input('Enter integer'))
#     return number ** 2
#
# res = square_2()
# print(res)


# def power(number_1, number_2):
#     res = number_1 ** number_2
#     return res
#
#
# res_ = power(3, 8)
#
# print(res_)
# print(power(2, 3))


# salary = 1000
# bonus = 600
#
#
# def info():
#     print(salary + bonus)
#
#
# def info_2():
#     bonus = 200
#     print(salary + bonus)
#
#
# def info_3():
#     salary = 1500
#     bonus = 200
#     print(salary + bonus)

#
# info()
# info_2()
# info_3()


# my_func = lambda number_1, number_2: number_1 + number_2
#
# print(my_func(6, 123))
#
#
# print(list(map(lambda  x: x**0.5, [1, 2, 3, 4, 5])))


students_list = [
    {'name': 'Василий', 'surname': "Теркин", 'gender':
     'М', 'program_exp':
     True, 'grade': [8, 8, 9, 10, 9], 'exam': 8},
    {'name': 'Мария', 'surname': "Павлова", 'gender':
     'Ж', 'program_exp':
     True, 'grade': [7, 8, 9, 7, 9], 'exam': 9},
    {'name': 'Ирина', 'surname': "Андреева", 'gender':
     'Ж', 'program_exp':
     False, 'grade': [10, 9, 8, 10, 10], 'exam': 7},
    {'name': 'Татьяна', 'surname': "Сидорова", 'gender':
     'Ж', 'program_exp':
     False, 'grade': [7, 8, 8, 9, 8], 'exam': 10},
    {'name': 'Иван', 'surname': "Васильев", 'gender':
     'М', 'program_exp':
     True, 'grade': [9, 8, 9, 6, 9], 'exam': 5},
    {'name': 'Роман', 'surname': "Золотарев", 'gender':
     'М', 'program_exp':
     False, 'grade': [8, 9, 9, 5, 9], 'exam': 6},
    ]

def get_avg_ex_grade(students, exp=None, gender=None):
    sum_ = 0
    counter = 0
    for student in students:
        if (student['program_exp'] == exp or exp is None) and (student['gender'] == gender or gender is None):
          sum_ += sum(student['grade']) / len(student['grade'])
          counter += 1
    return round(sum_ / counter, 2)
#
# print(get_avg_ex_grade(students_list))
# print(get_avg_ex_grade(students_list, True))
# print(get_avg_ex_grade(students_list, False))
#
# print(get_avg_ex_grade(students_list, True, 'Ж'))
# print(get_avg_ex_grade(students_list, False, 'М'))
#
# print(get_avg_ex_grade(students_list, True, 'М'))
# print(get_avg_ex_grade(students_list, False, 'Ж'))


def main(students):
    while True:
        command = input('Enter your command')
        if command == '1':
            print(get_avg_ex_grade(students))
        elif command == '2':
            print(get_avg_ex_grade(students, True))
        elif command == '3':
            print(get_avg_ex_grade(students, False, 'М'))
        elif command == 'q':
            print('Exit')
            break


main(students_list)