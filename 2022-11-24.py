#1
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n=int(input("Value:"))
rst=factorial(n)
print("%d! = %d"%(n,rst))
'''
#2
'''
def factorial(n):
    val = n
    for i in range(n-1,0,-1):
        val = val * i
    return val
    
n=int(input("Value: "))
rst=factorial(n)
print("%d! = %d"%(n,rst))
'''
#3
'''
import random

for i in range(3):
    print(random.random())

print()

for i in range(5):
    print(random.random()*10)
'''
#4
'''
import random

sText = "abcdefg"
seqList = [1,2,3,4,5]
print("Count randint() randrange() choice() choice()")

for i in range(5):
    print("%4d %8d %11d %8s %8d"
          %((i,random.randint(1,6),
             random.randrange(1,7),
             random.choice(sText),
             random.choice(seqList))))                        
'''
#5
'''
def percent(pnum,tnum):
    return(pnum / tnum) * 100
n1 = int(input("전체 값: "))
n2 = int(input("일부 값: "))
p = percent(n2,n1)
print("%d의 %d은 %d%%입니다"%(n1,n2,p))
'''
#6
'''
def percent(pnum,tnum):
    return(tnum * pnum) / 100
n1 = int(input("전체 값: "))
n2 = int(input("퍼센트(%): "))
v = percent(n1,n2)
print("%d의 %d%%는 %d입니다"%(n1,n2,v))
'''
#7
'''
import random
for i in range(5):
    print(random.randint(0,3))
print()
for i in range(10):
    print(random.randrange(0,8))
'''
#8
'''
def percent(pnum,tnum):
    return(pnum / tnum) * 100
n1 = int(input("월급 : "))
n2 = int(input("음식/식료품비: "))
p = percent(n2,n1)
print("%d%%를 소비하였습니다."%p)
'''

