# students = ['Ivan', 'Masha', 'Sasha']
# teachers = ['Oleg', 'Alex']
#
# print(students + teachers)
# print(len(students))
#
#
# print([0, 1] * 4)
#
#
# students[1] = 'Oleg'
# print(students)
#
#
# students.append('Olga')
# print(students)
#
# students += ['Olga']
# print(students)
#
#
# students += ['Boris', 'Sergey']
# print(students)
#
#
# students.insert(1, 'Olga')
# print(students)
#
#
# students.remove('Sasha')
# print(students)
#
#
# del students[0]
# print(students)


# students = ['Ivan', 'Masha', 'Sasha']
# if 'Ivan' in students:
#     print('Ivan is here!')
# if 'Ann' not in students:
#     print('Ann is out')
#
#
# ind = students.index('Sasha')
# print(ind)
#
#
# ordered_students = sorted(students)
# # print(ordered_students) сам список не меняется
#
# students.sort()
# print(students)
#
#
#
# students.reverse()
# print(students)
# reversed(students)
# print(students[::-1])
#
#
# a = [1, 'A', 2]
# b = a
# a[0] = 42
# print(a)
# print(b)
#
#
#
# b[2] = 30
# print(b)
# print(a)
#
#
# a = [0] * 5
# print(a)
# a = [0 for i in range(5)]
# print(a)
#
# a = [i * i for i in range(5)]
# print(a)
#
# a = [int(i) for i in input().split()]
# print(sum(a))
#
# print(sum(int(i) for i in input().split()))
#
# s = 0
# for i in input().split():
#     s += int(i)
# print(s)


# a = [int(i) for i in input().split()]
# s = []
# if len(a) == 1:
#     print(a[0])
# else:
#     for i in range(len(a)):
#         print(a[i - 1] + a[(i + 1) % len(a)], end=" ")
#

a = [int(i) for i in input().split()]
n = len(a)
if n == 1:
    print(a[0])
else:
    for i in range(n - 1):
        print(a[i-1] + a[i+1], end=' ')
    print(a[n-2] + a[0])


ls = [int(i) for i in input().split()]
ls.sort()
j = 1
new = []
for i in ls:
    if i != j:
        j == i
    elif j == i








