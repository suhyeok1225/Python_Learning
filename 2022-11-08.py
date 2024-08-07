#1
'''
import turtle as t

def print_key(char):
    print(char,end="")
def key_a():
    print_key("a")
def key_sp():
    print_key("s_")
def key_sr():
    print_key("s^")
s=t.Screen()
s.onkey(key_a,"a")
s.onkeypress(key_sp,"s")
s.onkeyrelease(key_sr,"s")
s.onkey(s.bye,"q")
s.listen()
'''
#2
'''
gv=3

def func1():
    lv1=1
    lv1=lv1+gv
    print(lv1)
def func2(pv):
    lv2=pv
    print(lv2)
func1()
func2(2)
print(gv)
'''
#3
'''
gv=3
def func1():
    lv1=1
    gv=1
    lv1=lv1+gv
    print(lv1)
def func2(pv):
    lv2=pv
    print(lv2)
func1()
func2(2)
print(gv)
'''
#4
'''
gv=3
def func1():
    global gv
    lv1=1
    lv1=lv1+gv
    gv=1
    print(lv1,gv)
def func2(pv):
    lv2=pv
    print(lv2)
func1()
func2(2)
print(gv)
'''
#5
'''
import turtle as t
def print_digit(char):
    print(n,end="")
def key_1():
    print_digit("1")
def key_2():
    print_digit("2")
def key_3():
    print_digit("3")
s=t.Screen()
s.onkey(key_1,"1")
s.onkey(key_2,"2")
s.onkey(key_3,"3")
s.listen()
'''
#6
'''
a=1
def func(d):
    global a
    b=a+2
    c=b+d
    print("func:",a,b,c,d)
    a=c
    print("func:",a,b,c,d)
    return c

print("main:",a)
e=func(3)
print("main:",a,e)
'''
#7
'''
a=[1,2]
b=range(3)
c=[a,b,[4],[5,6]]
print(a,a[0],a[1])
print(b,b[0],b[1],b[2])
print(c)
print(c[0][0],c[1][2],c[2][0],c[3][0])
'''
#8
'''
a=[0,1,2,3,4,5]
for i in range(6):
    print(a[i],end=" ")
'''    
