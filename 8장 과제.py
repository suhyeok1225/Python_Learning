#1
'''
str=input("문자열:")
result1="";
result2="";
for i in range(len(str)):
    result1=result1+str[i]
   
for j in range(len(str)-1,-1,-1):
    result2=result2+str[j]
print("개별 문자 출력:",result1)
print("역순 개별 문자 출력:",result2)
'''
#2
'''
deg={10:'A',9:'A',8:'B',7:'C',6:'D',5:'F',4:'F',3:'F',2:'F',1:'F',0:'F'}
score=int(input("점수:"))
print(deg[score//10])
'''
#3
'''
items ={"라면":650, "우유":1100, "콜라":1200, "캔커피":500, "과자":700}
s=0
while True:
    it= input("제품명:")
    if it == "라면":
        s= s+items[it]
        print("[%s:%d]> %d"%(it,items[it],s))
    elif it == "우유":
        s= s+items[it]
        print("[%s:%d]> %d"%(it,items[it],s))  
    elif it == "콜라":
        s= s+items[it]
        print("[%s:%d]> %d"%(it,items[it],s))    
    elif it == "캔커피":
        s= s+items[it]
        print("[%s:%d]> %d"%(it,items[it],s))
    elif it == "과자":
        s= s+items[it]
        print("[%s:%d]> %d"%(it,items[it],s))    
    elif it =="":
        print("총 금액 :",s)
        break;
        
    else:
         print(it,"는 미등록 제품입니다.")
'''         
#4
'''
import math
x=float(input("실수:"))
print(x,":",math.ceil(x))
print(x,":",math.floor(x))
print(x,":",math.trunc(x))
'''
#5
'''
sales={1:8,2:6,3:10,4:13}
for i in sales:
    print(i,"분기:",'#'*sales[i])
'''
#6
'''
engkor_dict=dict()
while True:
    eng=input("영어단어:")
    kor=input("한글단어:")
    if eng==""and kor=="":
        break
    engkor_dict[eng]=kor
print(engkor_dict)  
'''
#7
'''
engkor_dict=dict()
while True:      
    eng=input("영어단어:")
    if eng=="":
        break
    if len(engkor_dict)==0:
        print("사전이 비어 있습니다")
        print("단어를 추가합니다.")
        kor=input("한글단어:")
    elif eng not in engkor_dict:
        print(eng,"단어가 등록되어 있지 않습니다.")
        print("단어를 추가합니다.")
        kor=input("한글단어:")
    engkor_dict[eng]=kor
   
print(engkor_dict)
'''
