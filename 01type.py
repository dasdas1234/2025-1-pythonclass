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

colors1 = ['red', 'blue', 'green']
print(colors1[1])
print(colors1)
print(len(colors1))

cities = ['서울', '부산', '인천', '대전', '제주', '울산', '강진', '통영']
print(cities[:])
print(cities[0:5])
print(cities[5:])
print(cities[-9:]) # 리버스 인덱싱
print(cities[::2]) # 증가값(step) [시작:끝:증가값]
print(cities[::-1])  # 역으로 슬라이싱
print(cities[4::-2])
