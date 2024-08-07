#1
'''
def percent(pnum, tnum):
    return (tnum * pnum) / 100

n1 = int(input("대출금:"))
n2 = float(input("년 이자(%):"))
yv = percent(n1,n2)
mv = yv/12
print("월 이자는 %d입니다."%mv)
'''
#2 392p-1
'''
def rsum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
num = int(input("n:"))    
sum = rsum(num)
print("1+...+%d=%d"%(num,sum))

def rsum(n):
    if n <= 1:
        return 1
    else:
        return n + rsum(n-1)

num=int(input("1+...+n,n:"))
sum=rsum(num)
print("1+...+%d=%d"%(num,sum))
'''
#3 392p-3
'''
import random
sum=0
print("Random number:",end=" ")
for i in range(10):
    num=random.randint(1,100)
    sum=sum+num
    print(num,end=" ")
print()    
      
avg=(sum/10)
print("합: %d,평균: %5.2f"%(sum,avg))
'''
#4 393p-5
'''
import random
tnum=random.randint(1,100)
pnum=random.randint(1,100)
sum=tnum+pnum
n=int(input("%d+%d="%(tnum,pnum)))
if sum == n:
    print("올바른 답입니다")
else:
    print("답은%d입니다."%sum)
'''
#5 397p-4
'''
import random
num=random.randint(1,100)
cnt=0
while True:
    n=int(input("수 입력:"))
    cnt=cnt+1
    if n == -1:
        break
    if num > n:
        print("%d은(는) 큽니다."%n)
    elif num < n:
        print("%d은(는) 작습니다."%n)
    else:
        print("%d이(가) 일치합니다."%n)
        break

if n == -1:
    print("%d회 만에 게임을 포기하였습니다."%cnt)
else:
    print("%d회 만에 슷자를 맞추었습니다."%cnt)
'''
#6
'''
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
n = int(input("f(n), n:"))

for i in range(0,n+1):
    rst = fibo(i)
    print("fibo(%d) = %d"%(i,rst))
'''    
