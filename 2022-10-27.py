#1
'''
def fadd(n,m):
    s=n+m
    return s
a=3
b=4
r=fadd(a,b)
print("반환값=",r)
'''
#2
'''
def avg(a,b):
    s=(a+b)/2
    return s

in1=int(input("값1:"))
in2=int(input("값2:"))
r=avg(in1,in2)
print("평균=",r)
'''
#3
'''
def avg(a,b,c):
    s=(a+b+c)/3
    return s
in1=int(input("값1:"))
in2=int(input("값2:"))
in3=int(input("값3:"))
r=avg(in1,in2,in3)
print("평균:",r)
'''
#4
'''
def dispch(ch,n):
    for i in range(1,n+1):
        print(ch,end="")
    
char=input("문자입력:")
num=int(input("횟수입력"))
dispch(char,num)
'''
#5
'''
def maxnum(m,n):
    if m>=n:
        maxmn=m
    else :
        maxmn=n
    return maxmn
    
num1=int(input("숫자1:"))
num2=int(input("숫자2:"))
result=maxnum(num1,num2)
print("큰수 =",result)
'''
#6
'''
def pow_xy(x,y):  
    return x**y

print("3*2**4+5=",3*pow_xy(2,4)+5)
'''
#7
'''
def one2n_sum1(n):
    s=0
    for i in range(1,n+1):
        s=s+i
    return s    
num=int(input("자연수:"))
if num<1:
    print("입력된 수가 1보다 작습니다.")
else:
    print("1--",num,"=",one2n_sum1(num))    
'''
