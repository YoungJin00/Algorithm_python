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
# print('*를 출력합니다')
# n = int(input('몇 개를 출력할까요 ? :'))
# w = int(input('몇 개 마다 줄바꿈 할까요 ? : '))
#
# for _ in range(n // w):
#     print('*' * w)
#
# rest = n % w
# if rest:
#     print('*' * rest)

#1-16

# print('1부터 n까지 정수의 합을 구합니다')
#
# while True:
#     n = int(input('n값을 입력하세요 : '))
#     if n > 0:
#         break
#
# sum = 0
# i = 1
#
# for i in range(1, n+1):
#     sum += i
#     i += 1
# print(f'1부터 {n}까지 정수의 합은 {sum}입니다')

#1-17
#가로, 세로 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나열하기
area = int(input('직사각형의 넓이를 입력하세요 : '))

for i in range(1, area + 1):
    if i * i > area:
        break
    if area % i:
        continue
    print(f'{i} * {area // i }')
