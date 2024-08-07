#1
'''
a=10
b=3.546
ch='a'
st="abc"
print("Value = %d"%a)
print("Value = %-4d,%4d"%(a,a))
print("Value = %f"%b)
print("Value = %4.1f,%4.2f"%(b,b))
print("Value = %c"%ch)
print("Vlaue = %s"%st)
'''
#2
'''
st="Text Stirng"
print(st[0],st[1],st[len(st)-1])
for i in range(len(st)):
    print(st[i],end="")
print()
'''
#3
'''
st="Text Stirng"
if 'x' in st:
    print("Included")
else:
    print("Not included")
print("lenth: ",len(st))
st1="123"
st2="3.546"
print(st1,st2)
st3=st.replace('S','s')
print(st3)
st4="TextString"
print(st.upper())
print(st.lower())
print(st.isdigit(),st4.isdigit(),st1.isdigit())
print(st.isalpha(),st4.isalpha(),st1.isalpha())
print(st.isalnum(),st4.isalnum(),st1.isalnum())
'''
#4
'''
st=input("이름 입력:")
st2=st[0]+st[2]
print(st[0],st[2])
print(st2)
'''
#5
'''
st=input("이름 입력:")
if st.isalpha():
    st2=st.upper()
    print(st,st2)
elif st.isdigit():
    n=int(st)+1
    print(st,n)
'''
#6 319p-4
'''
jn="980910-1234567"
print("%s %s %s"%(jn[0:2],jn[2:4],jn[4:6]))
print("%c"%jn[-7])
print("%c %c %c"%(jn[-1],jn[-3],jn[-5]))
'''
#7 320p-5
'''
str="python"
for i in range(len(str)):
    str2=str[0:i+1]
    print(str2)
'''
#8 322p-1
'''
s=input("문자열:")
while True:
    c=input("문자:")
    if c=="":
        break
    if c in s:
        print("문자%c가 문자열%s에 존재함"%(c,s))
    else:
         print("문자%c가 문자열%s에 존재하지 않음"%(c,s))
'''
#9 323p-3
'''
list=[1,2,3]
cmd=[]
print(list)
indata=input("리스트 명령:")
cmd=indata.split()
if cmd[0]=="append":
    list.append(int(cmd[1]))
elif cmd[0]=="insert":
    list.insert(int(cmd[1]),int(cmd[2]))
print(list)    
'''
