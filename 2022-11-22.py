#1 324p-5
'''
import time
now=time.localtime()
inymd=input("주민등록번호 년월일:")
year=now.tm_year
age=year-(int(inymd[0:2])+1900)+1
print("나이:",age)
'''
#2 326p-8
'''
data=["Python","C","Java","C++","Swift","R"]
print(data)
idx=data.index("Swift")
if idx < len(data):
    data[idx] = "Objective-C"
idx=data.index("Java")
if idx < len(data):
    data.insert(idx,"C#")
data.remove("R")    
for i in range(len(data)):
    print(data[i] , end=" ")
'''   
#3
'''
data=["Python","C","Java","C++","Swift","R"]
print(data)
idx=data.index("Swift")

if idx < len(data):
    data[idx] = "Basic"
if idx < len(data):  
    data.append("C++")        
for i in range(len(data)):
    print(data[i] , end="")
'''
#4
def isbn_check(isbn):
    s=0

    for i in range(len(isbn)-1):      
        if (i+1) % 2 == 1:
            s = s + int(isbn[i]) * 1
        else:
            s = s + int(isbn[i]) * 3
    print("ISBN 1~12자리의 가중치 반영 합계: %d"%s)
                       
    t = s % 10
    chk = (10 -t) % 10
    print("ISBN 1~12자리의 체크 기호 값: %d"%chk)
                        
    if chk == int(isbn[12]):
        rst = 1
    else:
        rst = 0
    return rst

isbn=input("ISBN 13자리(-제외):")

if len(isbn) == 13:
    rst = isbn_check(isbn)
    if rst == 1:
        print("ISBN 코드 : %s는 검증되었습니다."%isbn)
    else:
        print("ISBN 코드 : %s는 검증되지 않았습니다."%isbn)

else:
    print("ISBN 코드 입력은 -를 제외하고 13 자리를 입력해주세요.")
