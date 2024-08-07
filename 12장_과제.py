#P392-2번
'''
def isum(n):
    s = 0
    for i in range(n+1):
        s = s + i
    return s

num = int(input("1 + ... + n, n : "))
sum = isum(num)
print("1 + ... + %d = %d"%(num, sum))
'''

#P393-4번
'''
import random
rannum = random.randint(1, 6)
n = int(input("예상값 : "))
if n >= 1 and n <= 6:
    if n == rannum:
        print("주사위 :", rannum, "- 맞추었습니다.")
    else:
        print("주사위 :", rannum, "- 맞추지 못하였습니다.")
else:
    print("1~6 숫자를 입력해주세요.")
'''

#p393-6번
'''
import random
op1 = random.randint(1, 9)
op2 = random.randint(1, 9)
val = op1 * op2
tmpstr = "%d * %d = "%(op1, op2)
n = int(input(tmpstr))
if n == val:
    print("올바른 답입니다.")
else:
    print("답은 %d입니다."%val)
'''

#P394-8번
'''
num = [ 33, 42, 14, 20, 5, 9, 30, 45, 90 ]
avg = sum(num) / len(num)
print(num, ", 평균:", avg)
p = int(input("초과 비율(%) : "))
avgp = avg * (1 + p / 100)
print("평균+초과 비율 값", avgp, end=" : ")
for i in range(len(num)):
    if num[i] > avgp:
        print(num[i], end=" ")
print("")
'''


#P397-3번
'''
import random
op1 = random.randint(1, 100)
op2 = random.randint(1, 100)
opnd = random.randint(1, 4)
if opnd == 1:
    val = op1 + op2
    opndstr = "+"
elif opnd == 2:
    val = op1 - op2
    opndstr = "-"
elif opnd == 3:
    val = op1 * op2
    opndstr = "*"
elif opnd == 4:
    val = op1 / op2
    opndstr = "/"
tmpstr = "%d %s %d = "%(op1, opndstr, op2)
n = int(input(tmpstr))
if n == val:
    print("올바른 답입니다.")
else:
    if opnd == 4:
        print("답은 %f입니다."%val)
    else:
        print("답은 %d입니다."%val)
'''


#398-5번
'''
pv = 30000000
rate = 0.034
nper = 1
yinterest = pv * rate
fv = pv + yinterest
drate = rate / 365
dinterest = pv * drate
print("원금 : %s원"%(format(pv, ",")))
print("이율(년) : %3.1f%%"%(rate*100))
print("기간(년) : %d"%nper)
print("이자(년) : %s원"%(format(int(yinterest), ",")))
print("이율(일) : %7.6f%%"%(drate*100))
print("이자(일) : %s원"%(format(int(dinterest), ",")))
'''


