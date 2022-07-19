#
# total = 0
# q = 0
# while True:
#     i = int(input())
#     total += i
#     q += i**2
#     if total == 0:
#         break
# print(q)
#
#
#
# s = [int(input())]
# while sum(s) != 0: s.append(int(input()))
# print(sum([i**2 for i in s]))


# n = int(input())
# new = []
# for i in range(n+1):
#     count = 0
#     while count < i +1:
#         new.append(i+1)
#         count += 1
#         if n == len(new):
#             for j in new:
#                 print(j, end=' ')
#             break


# n = int(input())
# a = []
# i = 0
# while len(a) < n:
#     a += [i] * i
#     i += 1
# print(*a[:n])



n = int(input())
if max(str(n)) == min(str(n)):
    print('YES')
else:
    print('NO')



n = int(input())
while n % 10 == n // 10 % 10:
    n //= 10
print('YES' if n < 10 else 'NO')


x = input()
print('YES' if max(x) == min(x) else 'NO')


