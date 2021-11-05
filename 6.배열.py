#2-1
#학생 5명의 시험점수를 입력받아 합계와 평균을 출력

# print('학생 그룹 점수의 합계와 평균을 구합니다.')
#
# a1 = int(input('학생1의 점수를 입력하세요 : '))
# a2 = int(input('학생2의 점수를 입력하세요 : '))
# a3 = int(input('학생3의 점수를 입력하세요 : '))
# a4 = int(input('학생4의 점수를 입력하세요 : '))
# a5 = int(input('학생5의 점수를 입력하세요 : '))
#
# total = 0
# total+=a1
# total+=a2
# total+=a3
# total+=a4
# total+=a5
#
# print(f'총점 = {total}, 평균 = {total / 5}')


#2-3
# from max import max_of
#
# print('배열의 최댓값을 구합니다.')
# print('주의 : "End"를 입력하면 종료합니다.')
#
# number =0
# x = []
#
# while True:
#     s = input(f'x[{number}]값을 입력하세여 : ')
#     if s == 'End':
#         break
#     x.append(int(s))
#     number +=1
#
# print(f'{number}개를 입력했습니다. ')
# print(f'최댓값은 {max_of(x)}입니다.')

#2-4

# import random
# from max import max_of
#
# print('난수의 최댓값을 구합니다.')
# num = int(input('난수의 개수를 입력하세요 : '))
# lo = int(input('난수의 최솟값을 입력하세요 : '))
# hi = int(input('난수의 최댓값을 입력하세요 : '))
# x = [None] * num
#
# for i in range(num):
#     x[i] = random.randint(lo, hi)
#
# print(f'{(x)}')
# print(f'이 가운데 최댓값은 {max_of(x)} 입니다.')

#2-6
# from typing import Any, MutableSequence
#
# def reverse_array(a: MutableSequence) -> None:
#     n = len(a)
#     for i in range(n // 2):
#         a[i], a[n - i -1] = a[n - i -1], a[i]
#
# if __name__ == '__main__':
#     print('배열 원소를 역순으로 정렬합니다.')
#     nx = int(input('원소 수를 입력하세요 : '))
#     x = [None] * nx
#
#     for i in range(nx):
#         x[i] = int(input(f'x[{i}]값을 입력하세요 : '))
#
#     reverse_array(x)
#     print('배열 원소를 역순으로 정렬했습니다.')
#     for i in range(nx):
#         print(f'x[{i}] = {x[i]}')

#2-8
#1000이하 소수 나열

# counter = 0
# for n in range(2, 1001):
#     for i in range(2, n):
#         counter += 1
#         if n % i == 0:
#             break
#     else:
#         print(n)
# print(f'나눗셈을 실행한 횟수 : {counter}')

#2-9
# counter = 0
# ptr = 0 #이미 찾은 소수의 개수
# prime = [None] * 500
#
# prime[ptr] = 2 #2는 소수이므로 초깃값으로 지정
# ptr += 1
#
# for n in range(3, 1001, 2): #홀수만을 대상으로
#     for i in range(1, ptr): #이미 찾은 소수로 나눔
#         counter += 1
#         if n % prime[i] == 0:
#             break
#     else:
#         prime[ptr] = n
#         ptr += 1
#
# for i in range(ptr):
#     print(prime[i])
# print(f'나눗셈을 실행한 횟수 : {counter}')

#2-10
counter = 0
ptr = 0
prime = [None] * 500

prime[ptr] = 2
ptr += 1

prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2):
    i = 1
    while prime[i] * prime[i] <= n:
        counter +=2
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        counter +=1

for i in range(ptr):
    print(prime[i])
print(f'나눗셈을 실행한 횟수 : {counter}')