#1
'''
b=[[0,1],[2,3],[4,5],[6,7]]
for i in range(4):
    for j in range(2):
        print(b[i][j],end="")
    print()   
'''
#2 282p-2
'''
a=b=c=1
def func():
    global a,b,c
    a=b=c=2
    print("func:",a,b,c)
    
print("main:",a,b,c)
func()
print("main:",a,b,c)
'''
#3 283p-3
'''
a=b=c=1

def func1():
    a=b=c=2
def func2():
    global a,b
    a=b=3
    c=3

print(a,b,c)
func1()
print(a,b,c)
func2()
print(a,b,c)
'''
#4 285p-8
'''
data=[[21,7,41,65],[2,8,72,52]]
for i in range(len(data)):
    for j in range(len(data[0])):
        print(data[i][j],end=" ")
    print("")    
'''
#5 286p-1
'''
data=[21,7,43,65,2,8,72,52,9]
search=int(input("찾을 값:"))
find=len(data)

for i in range(len(data)):
    if search==data[i]:
        find=i     
        break
if find<len(data) :
    print("위치:",find+1)
else:
    print("찾지못함")   
'''
#6 287p-3

data=[[21,7,43,65],[2,8,72,52]]
search=int(input("찾을 값:"))
find=len(data)
fin=len(data[0])
for i in range(len(data)):
    for j in range(len(data[0])):
        if search==data[i][j]:
            find=i
            fin=j
            break
if find<len(data) and fin<len(data[0]):
    print("위치:",find+1,"행",fin+1,"열")
else:
    print("찾지못함")        
        
#7 288p-7
'''
data=[10,20,30,40,0]
lenc=len(data)-1
for i in range(lenc):
    data[lenc]=data[lenc]+data[i]
    print(data[i],end="")
    if(i<lenc-1):
        print("+",end="")
print("=",data[lenc])       
'''    
