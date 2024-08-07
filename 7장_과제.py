#P195-4번
'''
def print_str(st, cnt):
    for i in range(cnt):
        print(st)

s = input("문자열 : ")
c = int(input("횟수 : "))
print_str(s, c)
'''

#P196-9번
'''
def rectangle_area(col, row):
    area = col * row
    return area

c = int(input("가로 : "))
r = int(input("세로 : "))
result = rectangle_area(c, r)
print("가로", c, "세로", r, "인 사각형의 넓이 =", result)
'''


#P198-2번
'''
def one2nt_sum(n):
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s

num = int(input("자연수 : "))
if num < 1 or num > 10:
    print("입력값의 범위를 초과하였습니다.")
else:
    numt = num * 10
    result = one2nt_sum(numt)
    print("1 --", numt, "=", result )
'''

#P200-5번
'''
def pzn(num):
    if num > 0:
        tmp = 1
    elif num == 0:
        tmp = 0
    else:
        tmp = -1
    return tmp

while True:
    n = int(input("정수 : "))
    r = pzn(n)
    if r == 1:
        print("양수")
    elif r == 0:
        print("0")
        break
    else:
        print("음수")
'''


