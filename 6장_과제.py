#p164-5번
'''
s1 = 0
s2 = 0
for i in range(1, 101):
    if (i % 2 == 1):
        s1 = s1 + i
    else:
        s2 = s2 + i
print("홀수 합 :", s1)
print("짝수 합 :", s2)
'''

#p165-7번
'''
y = 0
for i in range(1, 11):
    y = y + 1 / i
    print(y)
'''


#p166-9번
'''
y = 0
sign = -1
for i in range(1, 11):
    sign = sign * -1
    y = y + sign * 1 / i
    print(y)
'''


#p166-10번
'''
n = int(input("단 : "))
if n >= 2 and n <= 9:
    for i in range(1, 10):
        print(n, "*", i, "=", n*i)
'''


#p168-15번
'''
pw = ""
while pw != "pwpass":
    pw = input("비밀번호 : ")
print("LogIn Pass!!")
'''


#p170-1번
'''
maxnum = -9999
minnum = 9999
num = [ 8, 7, 3, 2, 9, 4, 1, 6, 5 ]
for i in num:
    if i > maxnum:
        maxnum = i
    if i < minnum:
        minnum = i
print("최댓값 :", maxnum)
print("최솟값 :", minnum)
'''

#p172-5번
'''
for i in range(0, 101, 10):
    f = i * 9 / 5 + 32
    k = i + 273.15
    print(i,"도 일때 ", "  화씨 =",f,"  섭씨 = ", k)
'''



