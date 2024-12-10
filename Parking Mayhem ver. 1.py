import turtle as trtl
import keyboard
import math
from PIL import Image
import random as rand
import time

wn = trtl.Screen()
wn.setup(1, 1)
wn.bgcolor(60/255, 60/255, 60/255)

Drifting = False
complete = False
c_errors = 0
instantAngle = 0
realAngle = 90
speed = 0
shiftAmount = 3

wn.addshape('Parking Mayhem Level Complete Screen.gif')
wn.addshape('Parking Mayhem Title Screen.gif')
wn.addshape('BlockGoal.gif')
wn.addshape('BlockBare.gif')
wn.addshape('BlockAngledAlt.gif')
wn.addshape('BlockSplit.gif')
wn.addshape('BlockBorder.gif')

wn.register_shape("Drift Car.gif")

occupied_spaces = [(0, 0)]

car = trtl.Turtle(shape='Drift Car.gif')
car.penup()

border = trtl.Turtle(shape='BlockBorder.gif')

a = trtl.Turtle(shape='BlockBare.gif')
a.shapesize(5)
b = trtl.Turtle(shape='BlockBare.gif')
b.shapesize(5)
c = trtl.Turtle(shape='BlockBare.gif')
c.shapesize(5)
d = trtl.Turtle(shape='BlockBare.gif')
d.shapesize(5)
e = trtl.Turtle(shape='BlockBare.gif')
e.shapesize(5)
f = trtl.Turtle(shape='BlockSplit.gif')
f.shapesize(5)
g = trtl.Turtle(shape='BlockSplit.gif')
g.shapesize(5)
h = trtl.Turtle(shape='BlockSplit.gif')
h.shapesize(5)
i = trtl.Turtle(shape='BlockSplit.gif')
i.shapesize(5)
j = trtl.Turtle(shape='BlockSplit.gif')
j.shapesize(5)
k = trtl.Turtle(shape='BlockAngledAlt.gif')
k.shapesize(5)
l = trtl.Turtle(shape='BlockAngledAlt.gif')
l.shapesize(5)
m = trtl.Turtle(shape='BlockAngledAlt.gif')
m.shapesize(5)
n = trtl.Turtle(shape='BlockAngledAlt.gif')
n.shapesize(5)
o = trtl.Turtle(shape='BlockAngledAlt.gif')
o.shapesize(5)

goal = trtl.Turtle(shape='BlockGoal.gif')

screen = trtl.Turtle(shape='Parking Mayhem Level Complete Screen.gif')
screen.hideturtle()
title_screen = trtl.Turtle(shape='Parking Mayhem Title Screen.gif')

def intervals(intv1, intv2):
    if rand.choice([True, False]):
        return rand.randrange(intv1[0], intv1[1], 100)
    else:
        return rand.randrange(intv2[0], intv2[1], 100)
    
if (0, 0) in occupied_spaces:
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------')
    print('             Overlap detection functioning nominally. Compounding errors reported:', c_errors)
    print('             Proceeding with program initiation protocols.')
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------')
    print('-- Beginning map generation. Steps remaining: 16')

def aset():
    a.penup()
    trtl.tracer(False)
    a.goto(rand.randrange(-400, 401, 100), rand.randrange(-400, 401, 100))
    if (a.xcor(), a.ycor()) in occupied_spaces:
        print('Block A (type Bare) was moved due to a collison with an existing object')
        aset()
    else:
        occupied_spaces.append((a.xcor(), a.ycor()))
        print('Added Block A (type Bare) coordiantes to Occupied Spaces list. Appended values', a.xcor(), a.ycor())
        print('-- Steps remaining: 15')
    trtl.tracer(True)

def bset():
    b.penup()
    trtl.tracer(False)
    b.goto(rand.randrange(-400, 401, 100), rand.randrange(-400, 401, 100))
    if (b.xcor(), b.ycor()) in occupied_spaces:
        print('Block B (type Bare) was moved due to a collison with an existing object')
        bset()
    else:
        occupied_spaces.append((b.xcor(), b.ycor()))
        print('Added Block B (type Bare) coordiantes to Occupied Spaces list. Appended values', b.xcor(), b.ycor())
        print('-- Steps remaining: 14')
    trtl.tracer(True)

def cset():
    c.penup()
    trtl.tracer(False)
    c.goto(rand.randrange(-400, 401, 100), rand.randrange(-400, 401, 100))
    if (c.xcor(), c.ycor()) in occupied_spaces:
        print('Block C (type Bare) was moved due to a collison with an existing object')
        cset()
    else:
        occupied_spaces.append((c.xcor(), c.ycor()))
        print('Added Block C (type Bare) coordiantes to Occupied Spaces list. Appended values', c.xcor(), c.ycor())
        print('-- Steps remaining: 13')
    trtl.tracer(True)

def dset():
    d.penup()
    trtl.tracer(False)
    d.goto(rand.randrange(-400, 401, 100), rand.randrange(-400, 401, 100))
    if (d.xcor(), d.ycor()) in occupied_spaces:
        print('Block D (type Bare) was moved due to a collison with an existing object')
        dset()
    else:
        occupied_spaces.append((d.xcor(), d.ycor()))
        print('Added Block D (type Bare) coordiantes to Occupied Spaces list. Appended values', d.xcor(), d.ycor())
        print('-- Steps remaining: 12')
    trtl.tracer(True)

def eset():
    e.penup()
    trtl.tracer(False)
    e.goto(rand.randrange(-400, 401, 100), rand.randrange(-400, 401, 100))
    if (e.xcor(), e.ycor()) in occupied_spaces:
        print('Block E (type Bare) was moved due to a collison with an existing object')
        eset()
    else:
        occupied_spaces.append((e.xcor(), e.ycor()))
        print('Added Block E (type Bare) coordiantes to Occupied Spaces list. Appended values', e.xcor(), e.ycor())
        print('-- Steps remaining: 11')
    trtl.tracer(True)

def fset():
    f.penup()
    trtl.tracer(False)
    f.goto(rand.randrange(-400, 401, 100), rand.randrange(-400, 401, 100))
    if (f.xcor(), f.ycor()) in occupied_spaces:
        print('Block F (type Split) was moved due to a collison with an existing object')
        fset()
    else:
        occupied_spaces.append((f.xcor(), f.ycor()))
        print('Added Block F (type Split) coordiantes to Occupied Spaces list. Appended values', f.xcor(), f.ycor())
        print('-- Steps remaining: 10')
    trtl.tracer(True)

def gset():
    g.penup()
    trtl.tracer(False)
    g.goto(rand.randrange(-400, 401, 100), rand.randrange(-400, 401, 100))
    if (g.xcor(), g.ycor()) in occupied_spaces:
        print('Block G (type Split) was moved due to a collison with an existing object')
        gset()
    else:
        occupied_spaces.append((g.xcor(), g.ycor()))
        print('Added Block G (type Split) coordiantes to Occupied Spaces list. Appended values', g.xcor(), g.ycor())
        print('-- Steps remaining: 9')
    trtl.tracer(True)

def hset():
    h.penup()
    trtl.tracer(False)
    h.goto(rand.randrange(-400, 401, 100), rand.randrange(-400, 401, 100))
    if (h.xcor(), h.ycor()) in occupied_spaces:
        print('Block H (type Split) was moved due to a collison with an existing object')
        hset()
    else:
        occupied_spaces.append((h.xcor(), h.ycor()))
        print('Added Block H (type Split) coordiantes to Occupied Spaces list. Appended values', h.xcor(), h.ycor())
        print('-- Steps remaining: 8')
    trtl.tracer(True)

def iset():
    i.penup()
    trtl.tracer(False)
    i.goto(rand.randrange(-400, 401, 100), rand.randrange(-400, 401, 100))
    if (i.xcor(), i.ycor()) in occupied_spaces:
        print('Block I (type Split) was moved due to a collison with an existing object')
        iset()
    else:
        occupied_spaces.append((i.xcor(), i.ycor()))
        print('Added Block I (type Split) coordiantes to Occupied Spaces list. Appended values', i.xcor(), i.ycor())
        print('-- Steps remaining: 7')
    trtl.tracer(True)

def jset():
    j.penup()
    trtl.tracer(False)
    j.goto(rand.randrange(-400, 401, 100), rand.randrange(-400, 401, 100))
    if (j.xcor(), j.ycor()) in occupied_spaces:
        print('Block J (type Split) was moved due to a collison with an existing object')
        jset()
    else:
        occupied_spaces.append((j.xcor(), j.ycor()))
        print('Added Block J (type Split) coordiantes to Occupied Spaces list. Appended values', j.xcor(), j.ycor())
        print('-- Steps remaining: 6')
    trtl.tracer(True)

def kset():
    k.penup()
    trtl.tracer(False)
    k.goto(rand.randrange(-400, 401, 100), rand.randrange(-400, 401, 100))
    if (k.xcor(), k.ycor()) in occupied_spaces:
        print('Block K (type Angled) was moved due to a collison with an existing object')
        kset()
    else:
        occupied_spaces.append((k.xcor(), k.ycor()))
        print('Added Block K (type Angled) coordiantes to Occupied Spaces list. Appended values', k.xcor(), k.ycor())
        print('-- Steps remaining: 5')
    trtl.tracer(True)

def lset():
    l.penup()
    trtl.tracer(False)
    l.goto(rand.randrange(-400, 401, 100), rand.randrange(-400, 401, 100))
    if (l.xcor(), l.ycor()) in occupied_spaces:
        print('Block L (type Angled) was moved due to a collison with an existing object')
        lset()
    else:
        occupied_spaces.append((l.xcor(), l.ycor()))
        print('Added Block L (type Angled) coordiantes to Occupied Spaces list. Appended values', l.xcor(), l.ycor())
        print('-- Steps remaining: 4')
    trtl.tracer(True)

def mset():
    m.penup()
    trtl.tracer(False)
    m.goto(rand.randrange(-400, 401, 100), rand.randrange(-400, 401, 100))
    if (m.xcor(), m.ycor()) in occupied_spaces:
        print('Block M (type Angled) was moved due to a collison with an existing object')
        mset()
    else:
        occupied_spaces.append((m.xcor(), m.ycor()))
        print('Added Block M (type Angled) coordiantes to Occupied Spaces list. Appended values', m.xcor(), m.ycor())
        print('-- Steps remaining: 3')
    trtl.tracer(True)

def nset():
    n.penup()
    trtl.tracer(False)
    n.goto(rand.randrange(-400, 401, 100), rand.randrange(-400, 401, 100))
    if (n.xcor(), n.ycor()) in occupied_spaces:
        print('Block N (type Angled) was moved due to a collison with an existing object')
        nset()
    else:
        occupied_spaces.append((n.xcor(), n.ycor()))
        print('Added Block N (type Angled) coordiantes to Occupied Spaces list. Appended values', n.xcor(), n.ycor())
        print('-- Steps remaining: 2')
    trtl.tracer(True)

def oset():
    o.penup()
    trtl.tracer(False)
    o.goto(rand.randrange(-400, 401, 100), rand.randrange(-400, 401, 100))
    if (o.xcor(), o.ycor()) in occupied_spaces:
        print('Block O (type Angled) was moved due to a collison with an existing object')
        oset()
    else:
        occupied_spaces.append((o.xcor(), o.ycor()))
        print('Added Block O (type Angled) coordiantes to Occupied Spaces list. Appended values', o.xcor(), o.ycor())
        print('-- Steps remaining: 1')
    trtl.tracer(True)

def goalset():
    goal.penup()
    trtl.tracer(False)
    goal.goto(intervals((-400, -300), (300, 400)), intervals((-400, -300), (300, 400)))
    if (goal.xcor(), goal.ycor()) in occupied_spaces:
        print('Block Goal (type Goal) was moved due to a collison with an existing object')
        goalset()
    else:
        occupied_spaces.append((goal.xcor(), goal.ycor()))
        print('Added Block Goal (type Goal) coordiantes to Occupied Spaces list. Appended values', goal.xcor(), goal.ycor())
        print('-- Steps remaining: 0')
    trtl.tracer(True)



def setup():
    border.showturtle()
    border.forward(0)
    
    aset()
    bset()
    cset()
    dset()
    eset()
    fset()
    gset()
    hset()
    iset()
    jset()
    kset()
    lset()
    mset()
    nset()
    oset()
    goalset()

    print('-----------------------------------------------------------------------------------------------------------------------------------------------------')
    print('             All objects have been succesfully generated. The list has', len(occupied_spaces), 'items, meaning that it was appended', (len(occupied_spaces)-1), 'times this sequence.')
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------')
    
def rotate_car(angle):
    image = Image.open("Drift Car.gif")
    rotated_image = image.rotate(angle, resample=Image.BICUBIC, expand=True)
    
    rotated_image.save("rotated_field.gif")
    wn.register_shape("rotated_field.gif")
    car.shape("rotated_field.gif")

setup()

wn.setup(960, 960)

time.sleep(3)

title_screen.hideturtle()

# Main loop
while True:
    if keyboard.is_pressed('w'):
        speed += 0.1
    
    if keyboard.is_pressed('s'):
        if speed > 0:
            speed -= 0.3

    if keyboard.is_pressed('d'):
        instantAngle = 0
        if instantAngle > -45:
            instantAngle -= math.sqrt(abs(speed))


    if keyboard.is_pressed('a'):
        instantAngle = 0
        if instantAngle < 45:
            instantAngle += math.sqrt(abs(speed))

    if keyboard.is_pressed('a') is False and keyboard.is_pressed('d') is False:
        instantAngle = 0

    if instantAngle < 0:
        realAngle -= shiftAmount

    if instantAngle > 0:
        realAngle += shiftAmount

    car.setheading(realAngle)
    if speed == 0:
        Drifting == False
    
    rotate_car(realAngle - 90)

    if (abs(car.xcor() - a.xcor()) <= 65) and (abs(car.ycor() - a.ycor()) <= 65):
        car.forward(2*-speed)
        speed = 0

    if (abs(car.xcor() - b.xcor()) <= 65) and (abs(car.ycor() - b.ycor()) <= 65):
        car.forward(2*-speed)
        speed = 0

    if (abs(car.xcor() - c.xcor()) <= 65) and (abs(car.ycor() - c.ycor()) <= 65):
        car.forward(2*-speed)
        speed = 0

    if (abs(car.xcor() - d.xcor()) <= 65) and (abs(car.ycor() - d.ycor()) <= 65):
        car.forward(2*-speed)
        speed = 0

    if (abs(car.xcor() - e.xcor()) <= 65) and (abs(car.ycor() -e.ycor()) <= 65):
        car.forward(2*-speed)
        speed = 0

    if (abs(car.xcor() - f.xcor()) <= 65) and (abs(car.ycor() - f.ycor()) <= 65):
        car.forward(2*-speed)
        speed = 0

    if (abs(car.xcor() - g.xcor()) <= 65) and (abs(car.ycor() - g.ycor()) <= 65):
        car.forward(2*-speed)
        speed = 0

    if (abs(car.xcor() - h.xcor()) <= 65) and (abs(car.ycor() - h.ycor()) <= 65):
        car.forward(2*-speed)
        speed = 0

    if (abs(car.xcor() - i.xcor()) <= 65) and (abs(car.ycor() - i.ycor()) <= 65):
        car.forward(2*-speed)
        speed = 0

    if (abs(car.xcor() - j.xcor()) <= 65) and (abs(car.ycor() - j.ycor()) <= 65):
        car.forward(2*-speed)
        speed = 0

    if (abs(car.xcor() - k.xcor()) <= 65) and (abs(car.ycor() -k.ycor()) <= 65):
        car.forward(2*-speed)
        speed = 0

    if (abs(car.xcor() - l.xcor()) <= 65) and (abs(car.ycor() - l.ycor()) <= 65):
        car.forward(2*-speed)
        speed = 0

    if (abs(car.xcor() - m.xcor()) <= 65) and (abs(car.ycor() - m.ycor()) <= 65):
        car.forward(2*-speed)
        speed = 0

    if (abs(car.xcor() - n.xcor()) <= 65) and (abs(car.ycor() - n.ycor()) <= 65):
        car.forward(2*-speed)
        speed = 0

    if (abs(car.xcor() - o.xcor()) <= 65) and (abs(car.ycor() - o.ycor()) <= 65):
        car.forward(2*-speed)
        speed = 0

    if (abs(car.xcor() - goal.xcor()) <= 10) and (abs(car.ycor() - goal.ycor()) <= 10):
        car.forward(2*-speed)
        speed = 0 
        complete = True

    if (car.xcor() > 430) or (car.xcor() < -430) or (car.ycor() > 430) or (car.ycor() < -430):
        car.forward(2*-speed)
        speed = 0

    if complete == True:
        screen.showturtle()
        if keyboard.is_pressed('enter'):
            speed = 0
            occupied_spaces = [(0, 0)]
            car.goto(0, 0)
            speed = 0
            realAngle = 90
            car.setheading(90)
            setup()
            time.sleep(0.25)
            screen.hideturtle()
            complete = False

    if keyboard.is_pressed('r'):
        complete = True
            


    car.forward(speed)