# num = int(input())
# flag = True
#
# for i in range(2, num):
#     if num % i == 0:
#         flag = False
#         break
#
# if flag == True:
#     print('Число простое')
# else:
#     print('Число составное')


# result = 0
# for i in range(10):
#     num = int(input())
#     if num < 0:
#         break
#     result += num
# print(result)


# num = int(input())
# number = num
# flag = False
# while num != 0:
#     last = num % 10
#     if last == 7:
#         flag = True
#         break
#     num //= 10
#
# if flag == True:
#     print(f'Число {number} содержит цифру 7')
# else:
#     print(f'Число {number}  не содержит цифру 7')


# for i in range(1, 101):
#     if i == 7 or i == 17 or i == 29 or i == 78:
#         continue
#     print(i)


# n = 10
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n, end='*')


# n = int(input())
#
# for i in range(n):
#     i += 1
#     if n % i == 0 and i != 1:
#         print(i)
#         break
#
#
# n = int(input())
# for i in range(2,n+1):
#     if n % i == 0:
#         print(i)
#         break


# n, div = int(input()), 2
# while n % div:
#     div += 1
# print(div)


# n = int(input())
# for i in range(1, n+1):
#     if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
#         continue
#     print(i)
#
# for i in range(1, int(input()) + 1):
#     if i in range(5, 10) or i in range(17, 38) or i in range(78, 88):
#         continue
#     print(i)


# [print(i) for i in range(1,int(input())+1) if not (5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87)]


# num = int(input())
# n = num
# while n != 0:
#     last = n % 10
#     if last == 7:
#         print('Число', num, 'содержит цифру 7')
#         break
#     n //= 10
# else:
#     print('Число', num, 'не содержит цифру 7')


# lst = [int(i) for i in input().split()]
# el = int(input())
# inn = []
# for ind,i in enumerate(lst):
#     if i == el:
#         inn.append(ind)
# if len(inn) == 0:
#     print('Отсутствует')
# else:
#     print(*inn)

l = [int(i) for i in input().split()]
x = int(input())
if x not in l:
    print('Отсутствует')
else:
    [print(i, end=' ') for i, z in enumerate(l) if z == x]

