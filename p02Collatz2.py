# 2025 4월2일 파이썬 수업 프로젝트 두번쨰
# 콜라츠 추측, 또는 우박수
# 1부터 1000까지 숫자중,가장 많은 단계를 거쳐서 1로가는 수는 무엇인가?, 가장 많은 단계는 몇단계인가?
# 규칙: n이 짝수 -> n/2
#      n이 홀수 -> 3n+1
#  예: 5 -> 16 -> 8 -> 4 -> 2 -> 1   (5단계)
from statistics import multimode

# 2025.4.9. 우박수 프로젝트 두번째: 기본 통계량 구하기
# numpy 배열, list 두가지 방식으로 시험
# 구하는 통계량: 평균, 중앙값, 표준편차, 최빈값, 최대값

import numpy as np
import statistics
import time

from p02Collatzfunc import collatz


MAXNUM = 100

ncounts = [collatz(n) for n in range(1, MAXNUM)]

# 리스트방식

start = time.time()
ncountl = []

for n in range(1,MAXNUM):
    ncount = collatz(n)
    ncountl.append(ncount)

# print(ncountl)
# print(sum(ncountl)/len(ncountl))

#평균, 중앙값, 표준편차, 최빈값, 최대값
nmax = 0
# 평균
print(f'평균={statistics.mean(ncountl):,.5f}')
print(f'최대값={max(ncountl)}')
print(f'중앙값={statistics.median(ncountl):,.5f}')
print(f'최빈값={statistics.multimode(ncountl)}')
print(f'표준편차={statistics.stdev(ncountl):,.5f}')
print(f'해당숫자{ncountl.index(max(ncountl))+1}')

end = time.time()
print(f'{end - start:.5f}초가 걸렸습니다.')

print("\n[리스트 상위 3개]")
numl123 = sorted([(val, idx+1) for idx, val in enumerate(ncounts)], reverse=True)[:3]
for i, (val, n) in enumerate(numl123, start=1):
    print(f'{i}위: 값={val}, 해당숫자={n}')

# numoy
start = time.time()
ncounta = np.zeros(MAXNUM-1)

for n in range(1,MAXNUM):
    ncount = collatz(n)
    ncounta[n-1] = ncount


#평균, 중앙값, 표준편차, 최빈값, 최대값

# 평균
print(f'평균={np.mean(ncounta)}')
print(f'최대값={np.max(ncounta):.5f}')
print(f'중앙값={np.median(ncounta)}')
print(f'최빈값={multimode(ncounta)}')
print(f'표준편차={np.std(ncounta):.5f}')
end = time.time()
print(f'{end - start:.5f}초가 걸렸습니다.')

print("\n[NumPy 상위 3개]")
nump123 = np.argsort(ncounta)[::-1][:3]
for i, idx in enumerate(nump123, start=1):
    print(f'{i}위: 값={int(ncounta[idx])}, 해당숫자={idx+1}')