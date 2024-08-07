#1
'''
num1=int(input("정수1:"))
num2=int(input("정수2:")) 

def div_qr():
    global num1,num2
    div=num1//num2
    res=num1%num2
    print("몫:",div,"나머지:",res) 
div_qr()
'''
#2
'''
num1=int(input("정수1:"))
num2=int(input("정수2:")) 

def div_qr():
    global num1,num2
    div=num1//num2
    res=num1%num2
    return(div,res)  
(di,re)=div_qr()
print("몫:",di,"나머지:",re)
'''
#3
'''
data=[21,7,43,65,2,8,72,52,9]
for i in range(len(data)-1,-1,-1):
    print(data[i],end=" ")
'''
#4
'''
data=[21,7,43,65,2,8,72,52,9]
search=int(input("찾을 배수:"))
find=len(data)
for i in range(len(data)):
    if data[i]%search==0:
        find=i
        print("위치:",find,"값:",data[i])
if find==len(data):
    print("찾지못함")
'''    
#5
'''
data=[[21,7,43,65],[2,8,72,52]]
print("행렬") 
for i in range(len(data)):
    for j in range(len(data[0])):      
        print(data[i][j],end=" ")
    print("")
print("")    
print("전치행렬")  
for i in range(len(data[0])):
    for j in range(len(data)):
        print(data[j][i],end=" ")
    print("")  
'''
#6
'''
data=[[10,20,30,40,0],[50,60,70,80,0],[90,100,110,120,0],[130,140,150,160,0],[170,180,190,200,0],[0,0,0,0,0]]

for i in range(len(data)-1):
    for j in range(len(data[0]-1)):      
        data[len(data)-1][len(data[0]-1)]=data[len(data)-1][len(data[0]-1)]+data[i][j]
        print(data[i][j],end="")

print(data[len(data)-1],data[len(data[0]-1)])
         
'''       
              


