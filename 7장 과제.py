#1
'''
def print_str(st,cnt):
    for i in range(1,cnt+1):
        print(st)

string=input("문자열:")
count=int(input("횟수:"))
print_str(string,count)
'''
#2
'''
def rectangle_area(col,row):
    area=col*row
    return area
    
c=int(input("가로:"))
r=int(input("높이:"))
area=rectangle_area(c,r)
print("가로",c,"세로",r,"인 사각형의 넓이 = ",area)
'''
#3
'''
def one2nt_sum(n):
    n=n*10
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum

num=int(input("자연수:"))
if num < 1:
    print("입력값의 범위를 초과하였습니다.")
    
else:  
    print("1 --",num*10,"=",one2nt_sum(num))
'''
#4
'''
def pzn(num):
    if n > 0:
        r=1
    elif n < 0:
        r=-1
    else:
        r=0
    return r
while True:
    n=int(input("정수:"))
    r=pzn(n)
    if r == 1:
        print("양수")
        continue
    elif r == -1:
        print("음수")
        continue
    else:
       print("0")
       break
'''
