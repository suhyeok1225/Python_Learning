#1
'''
def fc(temper,action):
    if action == 0:
        tmp=temper*1.8+32
        tmpact="C2F"
    else:
        tmp=(temper-32)/1.8
        tmpact="F2C"
    return(tmp,tmpact)
t=int(input("온도:"))
a=int(input("변환(o:C2F,1:F2C):"))
(rt,ra)=fc(t,a)
print(ra,":",t,"=>",rt)           
'''
#2
'''
def vsum(*num):
    s=0
    for i in num:
        s=s+i
    return s    

result1=vsum(2,3)
result2=vsum(2,3,4)
result3=vsum(2,3,4,5)
print("2+3=",result1)
print("2+3+4=",result2)
print("2+3+4+5=",result3)
'''
#3
'''
a=5
b=3
cho=input('+,-,*,/:')
if cho=='+':
    s=a+b

elif cho=='-':
    s=a-b
   
elif cho=='*':
    s=a*b
    
elif cho=='/':
    s=a/b
else:
    print("잘못입력")
    
print("결과:",s)
'''
#4
'''
def sum1(num1,num2):
    result=num1+num2
    return result
def sum2(num1,num2):
    result=num1-num2
    return result
def sum3(num1,num2):
    result=num1*num2    
    return result
def sum4(num1,num2):
    result=num1/num2
    return result
cho=input('+,-,*,/:')    
a=5
b=3
if cho=='+':
    s=sum1(a,b)

elif cho=='-':
    s=sum2(a,b)
   
elif cho=='*':
    s=sum3(a,b)
    
elif cho=='/':
    s=sum4(a,b)
else:
    print("잘못입력")
    
print("결과:",s)
'''
#5
'''
comp_dict={'A':'T','T':'A','C':'G','G':'C'}
print(comp_dict)
print(len(comp_dict))
print(comp_dict.keys())
print(comp_dict.values())
'''
#6
'''
digit_dict={1:'일',2:'이',3:'삼'}
print(len(digit_dict))
print(digit_dict.keys())
print(digit_dict.values())
print(digit_dict[3])
print(digit_dict[1])
'''
#7
'''
fruit={'사과':100,'바나나':50,'수박':1000}
print(len(fruit))
print(fruit.keys())
print(fruit.values())
print(fruit['사과'])
print(fruit['수박'])
'''
