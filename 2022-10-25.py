#1
'''
def fpython():
    print("python")
    print("파이썬")
fpython()

def ifpython():
    print("python")
print("파이썬")

ifpython()
'''
#2
'''
print("12345678")
print("홍길동")
print("12345678")
print("홍길동")
print()

for i in range(2):
    print("12345678")
    print("홍길동")
print()

def sn():
    print("12345678")
    print("홍길동")
sn()
sn()
print()

for i in range(2):
    def sn():
        print("12345678")
        print("홍길동")
    sn()
'''
#3
'''
def print19():
    for i in range(1,10):
        print(i,end="")
    print()    
print19()        
'''
#4
'''
def fadd(n,m):
    s=n+m
    print(n,"+",m,"=",s)
a=3
b=4
fadd(a,b)
'''
#5
''' 
def calc_gugudan(dan):
    
    for i in range(1,10):
        print(dan,"*",i,"=",dan*i,"")

d=int(input("단:"))
if d>0 and d<10:
    calc_gugudan(d)
else:
        print("다시입력")      
'''
#6
'''
def print19(st,ed):
    for i in range(st,ed+1):
        print(i,end="")
    print("")        
s=int(input("시작 입력:"))
e=int(input("끝 입력:"))
if s<e:
    print19(s,e)        
else:
    print("시작값이 끝값보다 작아야 한다.")
'''
