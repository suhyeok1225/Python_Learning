#1
'''
import turtle as t

color_status=["white","blue","red"]
alert_status=["정상","주의","화재"]
tempc=50

def check_fire():
    if tempc<80:
        status=0
    elif tempc<120:
        status=1
    else:
        status=2

    t.clear()
    t.home()
    t.pendown()
    t.fillcolor(color_status[status])
    t.begin_fill
    t.circle(20)
    t.end_fill()
    t.penup()
    t.goto(-22,50)
    t.write("%s: %d"%(alert_status[status],tempc))
    
def keyUp():
    global tempc
    if tempc<80:
        tempc=tempc+5
    else:
        tempc=tempc+10
    check_fire()    

def keyDown():
    global tempc
    if tempc<80:
        tempc=tempc-5
    else:
        tempc=tempc-10
    check_fire()

t.setup(300,300)
s=t.Screen()
t.hideturtle()
t.speed(0)
check_fire()
s.onkey(keyUp,"Up")
s.onkey(keyDown,"Down")
s.onkey(s.bye,"q")
s.listen()
'''
#2
'''
fruit=[]
fruit.append("사과")
fruit.append("배")
fruit.append("감")
print(fruit)
for i in range(len(fruit)):
    print(i,fruit[i])

fruit.insert(2,"딸기")
print(fruit)
for i in range(len(fruit)):
    print(i,fruit[i])
'''
#3
'''
fruit=["사과","배","딸기","감"]
print(fruit,len(fruit))
del fruit[2]
print(fruit,len(fruit))
del fruit[0:2]
print(fruit,len(fruit))
fruit.remove("감")
print(fruit,len(fruit))
'''
#4
'''
city=[]
city.append("부산")
city.append("대구")
city.append("대전")
for i in range(len(city)):
    print(i,city[i])
city.insert(0,"서울")
city.insert(3,"인천")
print(city)
'''
#5
'''
city=[]
city.append("부산")
city.append("대구")
city.append("대전")
for i in range(len(city)):
    print(i,city[i])
city.insert(0,"서울")
city.insert(3,"인천")
print(city)
city[3]="울산"
del city[1:3]
print(city)
'''
