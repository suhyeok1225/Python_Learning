#1
'''
s=0
for i in range(1,101,2):
    s=s+i
print("s:",s)

s=0
for i in range(2,101,2):
    s=s+i
print("s:",s)   
'''

#2
'''
y=0
s=0
for i in range(1,11):
    y=1/i
    s=s+y
    print(s)
print("s:",s)    
'''
#3
'''
y=0
sign=-1
s=0
for i in range(1,11):
    sign=sign*-1
    y=sign/i
    s=s+y
    print(s)
print("s:",s)
'''
#4
'''
s=0
n=int(input("단:"))
if n>=2 and n<=9:
    for i in range(1,10):
        s=n*i
        print(s)
'''
#5
'''
pw=input("비밀번호:")
while pw!="pwpass":
    pw=input("비밀번호:")
print("Login Pass!!")
'''
#6
'''
num = [8,7,3,2,9,4,1,6,5]

max_num= num[0]
for i in range(1,len(num)):
        if num[i] > max_num:
            max_num =num[i]   
print("최댓값 : ",max_num)
min_num = num[0]
for i in range(1,len(num)):
        if num[i] < min_num:
            min_num =num[i]
print("최솟값 : ",min_num)
'''
#7
'''
for i in range(0,101,10):
    fah=i*9 / 5+32
    abs=i + 273.15
    print(i,fah,abs)
'''
