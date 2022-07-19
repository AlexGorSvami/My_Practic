# ZAD1:
# my version:

print(*reversed (input()), sep='')

n = int(input())
while n != 0:
    print(n % 10, end = '')
    n = n // 10

print(input()[::-1])

# # Zad2:
# my version:


num = int(input())
num_max = max(str(num))
num_min = min(str(num))
print(f'Максимальная цифра равна {num_max}')
print(f'Минимальная цифра равна {num_min}')


n, x, m = int(input()), -1, 10
while n:
    x = max(x, n % 10)
    m = min(m, n % 10)
    n //= 10
print('Максимальная цифра равна', x)
print('Минимальная цифра равна', m)


x = str(input())
print('Максимальная цифра равна', max(x))
print('Минимальная цифра равна', min(x))

i = list(input())
print(f'Максимальная цифра равна {max(i)}\nМинимальная цифра равна {min(i)}')