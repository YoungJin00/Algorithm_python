# 난수 생성
# 1-18
import random

n = int(input('난수의 개수를 입력하세요. : '))

for _ in range(n):
    r = random.randint(10,99)
    print(r, end=' ')
    if r == 13:
        print('\n프로그램을 중단합니다')
        break
else:
    print('\n난수 생성을 종료합니다.')

#1-19

for i in range(1, 13):
    if i == 8:
        continue
    print(i, end=' ')
print()


#1-20
for i in list(range(1, 8)) + list(range(9,13)):
    print(i, end=' ')
print()