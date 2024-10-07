
# 1 & 2

# def sum1(n1, n2, n3):
#     return n1 + n2 + n3

# def sum2(l):
#     sum = 0
#     for e in l:
#         sum += e

# 3 & 4

# def max(*args):
#     max = None
#     for e in args:
#         if max is None or e > max:
#             max = e
#     return max
# print(max(-1, 3, 5, 2))

# def inv(s):
#     r = ""
#     for c in s:
#         r = c + r
#     return r

# print(inv('satrebla'))

# 5 & 6

# def count_letter(s):
#     r = 0
#     for c in s:
#         if c.upper() != c.lower():
#             r += 1
#     return r

# def count_digit(s):
#     r = 0
#     for c in s:
#         if c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
#             r += 1
#     return r

# s = 'Paulius Akvile Jonas Jonas 0 15'
# print(f'zodziu: {len(s.split())}, raidziu: {count_letter(s)}, skaitmenu: {count_digit(s)}')

# 7

# def is_pirminis(n):
#     for x in range(2, n):
#         if n % x == 0:
#             return False
#     return True

# print(is_pirminis(17))

# 8

# 9

# keliamieji_metai = [metai for metai in range(1900, 2100) if (metai % 400 == 0 or (metai % 4 == 0 and metai % 100 != 0))]

# metai = 2024
# print(f'{metai} metai keliamieji = {2024 in keliamieji_metai}')

#10

import datetime

nuo = datetime.datetime.strptime('2054 03 30', '%Y %m %d')

d = round((datetime.datetime.now() - nuo).total_seconds())
print(d)

# print('a'.islower())
# print('1'.islower())
# print('A'.islower())
# print('#'.islower())
