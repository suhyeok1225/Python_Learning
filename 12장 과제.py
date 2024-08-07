#1
'''
def isum(n):
    s=0
    for i in range(1,n+1):     
        if n <=1:
            return 1
        else :            
            return n + isum(n-1)
num=int(input("1+...+n, n: "))
sum=isum(num)
print("1+...+%d = %d"%(num,sum))
'''
#2
'''
import random
num=random.randint(1,6)

n=int(input("예상값 : "))
if num == n:
    print("주사위 : %d - 맞추었습니다."%num)
elif 0 < n and n < 7 :
    print("주사위 : %d - 맞추지 못하였습니다."%num)
else:
    print("1~6 숫자를 입력해주세요")
'''
#3
'''
import random
tnum=random.randint(1,9)
pnum=random.randint(1,9)
sum=tnum*pnum
n=int(input("%d * %d= "%(tnum,pnum)))
if sum == n:
    print("올바른 답입니다")
else:
    print("답은 %d입니다."%sum)
'''
#4
'''
num = [33,42,14,20,5,9,30,45,90]
avg = sum(num) / len(num)
print(num,"평균:",avg)
p=int(input("초과 비율(%) : "))
pavg = avg * (1 + p / 100)
print("평균 + 초과 비율 값 %3.1f:"%pavg,end=" ")
for i in range(len(num)):
    if num[i] > pavg:
        print(num[i],end=" ")
'''
#5
'''
import random
tnum = random.randint(1,100)
pnum = random.randint(1,100)
num = random.randint(1,4)
if num == 1:
    s = tnum + pnum
    n=int(input("%d+%d="%(tnum,pnum)))
    if s == n:
        print("올바른 답입니다")
    else:
        print("답은%d입니다."%s)
elif num == 2:
    s = tnum - pnum
    n=int(input("%d-%d="%(tnum,pnum)))
    if s == n:
        print("올바른 답입니다")
    else:
        print("답은%d입니다."%s)
            
elif num == 3:
    s = tnum * pnum
    n=int(input("%d*%d="%(tnum,pnum)))
    if s == n:
        print("올바른 답입니다")
    else:
        print("답은%d입니다."%s)
elif num == 4:
    s = tnum / pnum    
    n=float(input("%d/%d="%(tnum,pnum)))
    if s == n:
        print("올바른 답입니다")
    else:
        print("답은 %3.2f입니다."%s)
'''
#6
'''
pv = 30000000
pom_year = 3.4
prd_year = 1
interest_year = int(pv*(pom_year/100))
pom_data = pom_year/365
interest_data = int(interest_year/365)
print("원금: %s원"%(format(pv,",")))
print("이율(년): %1.1f%%"%pom_year)
print("기간(년) :%d"%prd_year)
print("이자(년) :%s원"%format(interest_year,","))
print("이율(일) :%1.6f%%"%pom_data)
print("이자(일) :%s원"%format(interest_data,","))
'''
