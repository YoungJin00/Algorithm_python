#1-21
#구구단 곱셈표

for i in range(1, 10):
    for j in range(1, 10):
        print(f'{j} * {i} = {i * j:3}', end=' ')
    print()

#1-22
print('왼쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
n = int(input('짧은 변의 길이를 입력하세요. : '))
for i in range(n):
    for j in range(i+1):
        print('*', end='')
    print()

#1-23
print('오른쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
n = int(input('짧은 변의 길이를 입력하세요. : '))

for i in range(n):
    for _ in range(n - i - 1):
        print(' ', end='')
    for _ in range(i + 1):
        print('*', end='')
    print()
