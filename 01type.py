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
print(f'{tc=} ===>{tf1=}')