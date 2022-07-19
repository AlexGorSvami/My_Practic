# students = ['Ivan', 'Masha', 'Sasha']

# for student in students:
#     print('Hello,' + student + '!')
#
#
# print(len(students))
# print(students[::2])
# print(students[::-1])


# teachers = ['Oleg', 'Alex']
# print(students + teachers)
#
#
#
# students[1] = 'Oleg'
# print(students)
# students.append('Olga')
# print(students)
# students += ['Olga']
# print(students)
# students += ['Boris', 'Sergey']
# print(students)
# students.insert(1, 'Olga')
# print(students)


# students.remove('Sasha')
# print(students)
# del students[0]
# print(students)


# if 'Ivan' in students:
#     print('Ivan is here!')
# if 'Ann' not in students:
#     print('Ann is out')
#
#
# ind = students.index('Sasha')
# print(ind)
# # ind = students.index('Ann')


# ordered_students = sorted(students)
# print(ordered_students)
# print(min(students))
# print(max(students))
# students.sort()
# print(students)
#
#
# students.reverse()
# print(students)
#
# reversed(students)
# print(students)
# print(students[::-1])


# a = [1, 'A', 2]
# b = a
# a[0] = 42
# print(a)
# print(b)
# b[2] = 30
# print(b)
# print(a)


# a = [0] * 5
# print(a)
# a = [0 for i in range(5)]
# print(a)
# a = [i * i for i in range(5)]
# print(a)
# a = [int(i) for i in input().split()]
# print(a)


# a = [1, 2, 3]
#
# print(a)
#
#
# print(*a)


# l = [int(i) for i in input().split()]
# dup = {x for x in l if l.count(x) > 1}
# print(*dup)
#
#
#
# a, c = [str(i) for i in input().split()], []
# for i in a:
#     if i not in c and a.count(i) > 1:
#         c.append(i)
#         print(i, end=' ')
#
#
# ls = [int(i) for i in input().split()]
# for i in set(ls):
#     if ls.count(i) > 1:
#         print(i, end=' ')
#
#
#
# a,b=[int(i) for i in input().split()],''
# a.sort()
# for i in range(len(a)-1):
#     if a[i]==a[i+1] and a[i]!=b:
#         print(a[i], end=' ')
#         b=a[i]


# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(a[1])
# print(a[1][1])


# n = 3
# a = [[0] * n] * n
# a[0][0] = 5
# print(a)
#
# a = [[0] * n for i in range(n)]
# print(a)
# a = [[0 for j in range(n)] for i in range(n)]
# print(a)


# a = [5, 8, 4, 3, 5, 7]
# m = 99
# print(min(a))
# for i in a:
#     if m > i:
#         m = i
#
# print(m)


# n, m, k = (int(i) for i in input().split())
# a = [[0 for j in range(m)] for i in range(n)]
# for i in range(k):
#     row, col = (int(i) - 1 for i in input().split())
#     a[row][col] = -1
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == 0:
#             for di in range(-1,2):
#                 for dj in range(-1,2):
#                     ai = i + di
#                     aj = j + dj
#                     if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
#                         a[i][j] += 1
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == -1:
#             print('*', end='')
#         elif a[i][j] == 0:
#             print('.', end='')
#         else:
#             print(a[i][j], end='')
#             print()
#
# print(a)


