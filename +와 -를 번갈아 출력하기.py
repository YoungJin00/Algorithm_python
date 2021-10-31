#1- 12

# print('+와 -를 번갈아 출력합니다')
# n = int(input('몇 개를 출력할까요 : '))
#
# for i in range(n):
#     if i % 2:
#         print('-', end='')
#     else:
#         print('+', end='')
#
# print()

#수정
# print('+와 -를 번갈아 출력합니다.')
# n = int(input('몇 개를 출력할까요 :'))
#
# for i in range(1, n+1):
#     if i % 2:
#         print('+', end='')
#     else:
#         print('-', end='')
#
# print()

#1-13
# print('+와 -를 번갈아 출력합니다.')
# n = int(input('몇 개를 출력할까요 :'))
#
# for _ in range(n // 2):
#     print('+-', end='')
#
# if n % 2:
#     print('+', end='')
# print()

#1-14
#*를 n개를 출력하되 w개 마다 줄바꿈
# print('*를 출력합니다')
# n = int(input('몇 개를 출력할까요 ? :'))
# w = int(input('몇 개 마다 줄바꿈 할까요 ? : '))
#
# for i in range(n):
#     print('*', end='')
#     if i % w == w -1:
#         print()
# if n % w:
#     print()

#1-15
print('*를 출력합니다')
n = int(input('몇 개를 출력할까요 ? :'))
w = int(input('몇 개 마다 줄바꿈 할까요 ? : '))

for _ in range(n // w):
    print('*' * w)

rest = n % w
if rest:
    print('*' * rest)

