# 2025.03.12
# 파이썬 수업 - 변수 , 타입 , 출력
# 타입 (형) - 정수 : int (integer)
#            실수 : float (floating point)
#            문자열 : str (string)
#            논리값 : bool (boolean)

title = '시간계산'
sec = 3700
min = sec / 60
bigger = min > sec
print(sec,min,bigger)
print(type(title),type(sec),type(min),type(bigger))

a = int(10.3) # floor 버림, ceiling 올림, round 반올림
b = float(10.3)
c = str(10.3)
print(a,b,c)
print(type(a),type(b),type(c))

sec1 = 1300; sec2 = 500
seca = sec1 + sec2
secs = sec1 - sec2
secm = sec1 * sec2
secd = sec1 / sec2
secq = sec1 // sec2
secr = sec1 % sec2
print(f'{seca=},{secs=},{secm=},{secd=},{secq=},{secr=}') # f string

# 화씨를 섭씨로 바꿈
# tc = (tf - 32) * 5/9
# tf = (tc * 9/5) +32

tf = 100
tc = 270
print(f'{tf=} ===>{tc=}')

tc1 = (tf - 32) * 5/9
print(f'{tf=} ===>{tc1=}')

tf1 = (tc * 9/5) + 32
print(f'{tc=} ===>{tf1=}');

print(2 ** 3 , 2 ** (1/2), 2 ** (-1/2))

# 사칙연산중에서 0으로 나누는 것은 허용하지 않는다.
# print(3/0)

a= 'True'
print(type(a))

a='3'
b=float(a)
print(b ** int(a))

a='3.5'
b=4
print(b * a)

# 인덱싱
colors = ['red', 'blue', 'green']
print(colors) # 리스트 전체 출력
print(colors[1]) # 리스트 두번째 원소 출력, 0부터 시작
print(colors) # 리스트 마지막 원소 출력
print(len(colors)) # 리스트 길이 출력

# 슬라이싱
cities = ['서울', '부산', '인천', '의정부', '대전', '강릉', '논산', '포항']
print(cities[0:7]) # cities[0:n] 0 ~ n-1까지 표시
print(cities[:7]) # 0부터 n-1까지(6번까지)
print(cities[:-1]) # 0부터 -2 까지
print(cities[3:]) #
print(cities[::]) # 모두 표시
print(cities[-4:]) # 뒤에서 4번째부터 표시
print(cities[:7:2])  # 0번부터 n-1(6번째)번까지 2칸 간격으로 표시
print(cities[::3]) # 처음부터 끝까지 3칸 간격으로 표시
print(cities[::-1]) # 처음부터 끝까지 거꾸로 표시
print(cities[4::-2]) #

# 리스트의 추가
colors = ['red', 'blue', 'green']
colors.append('white') # white를 추가
print(colors[:])
colors.extend(['black', 'purple']) # 여러개 추가
print(colors[:])
colors.insert(1, 'orange')
print(colors[:])
colors.remove('purple')
print(colors[:])
colors[1] = 'sky'
print(colors[:])

#패킹, 언패킹
c1, _, c2, c3, _, _ = colors
print(c1, c2, c3)

# 연습문제
first = ["egg","salad", 'bread',"soup", "canafe"]
second = ["fish","lamb", "pork", "beef", "chicken"]
third = ["apple","banana", "orange", "grape", "mango"]

order = [first, second, third]
john = [order[0][:-2], second[1::3], third[0]]
del john[2]
john.extend([order[2][0:1]])
print(john)