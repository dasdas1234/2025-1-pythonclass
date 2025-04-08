# 2025 4월2일 파이썬 수업 프로젝트 두번쨰
# 콜라츠 추측, 또는 우박수
# 1부터 1000까지 숫자중,가장 많은 단계를 거쳐서 1로가는 수는 무엇인가?, 가장 많은 단계는 몇단계인가?
# 규칙: n이 짝수 -> n/2
#      n이 홀수 -> 3n+1
#  예: 5 -> 16 -> 8 -> 4 -> 2 -> 1   (5단계)
from mkl import second

n = 9


# n을 1부터 99까지 변화하면서, 각각의 단계수를 출력할 것
# 그중 가장 큰 수를 찾을 것

maxvalue = 0
maxvaluen = 0

secondvalue = 0
secondvaluen = 0

thirdvalue = 0
thirdvaluen = 0

for n in range(1,100):
    print(f'{n=}')
    ncount = 0
    i = n

    while i != 1:

        if i % 2 == 0:
            i = i // 2
        else:
            i = 3 * i + 1
        ncount = ncount + 1

    print(f"{ncount}번만에 1로 도착")
    if maxvalue < ncount:
        thirdvalue = secondvalue
        thirdvaluen = secondvaluen
        secondvalue = maxvalue
        secondvaluen = maxvaluen

        maxvalue = ncount
        maxvaluen = n
    elif secondvalue < ncount and secondvaluen > ncount:
        thirdvalue = secondvalue
        thirdvaluen = secondvaluen

        secondvalue = ncount
        secondvaluen = n
    elif thirdvalue < ncount and thirdvaluen > ncount:
        thirdvalue = ncount
        thirdvaluen = n


    print(f'{maxvalue=}, {maxvaluen=},{secondvalue=},{secondvaluen=},{thirdvalue=},{thirdvaluen=}')
