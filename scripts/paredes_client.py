#! /usr/bin/env python3

import sys

try:
    from pymorse import Morse
except ImportError:
    print("you need first to install pymorse, the Python bindings for MORSE!")
    sys.exit(1)

v = 0.0
w = 0.0
x = 100
y = 100

def distFront(sensor):
    global x, w
    if sensor['point_list'][5][0] == 0:
        x = 100
    else:
        x = sensor['point_list'][5][0]

def distSide(sensor):
    global y
    if sensor['point_list'][5][0] == 0:
        y = 100
    else:
        y = sensor['point_list'][5][0]
        y = y - 2.5 # Offset for the integral

with Morse() as simu:
    motion = simu.Walle.motion
    motion.publish({"v": v, "w": w})
    pose = simu.Walle.pose
    simu.Walle.sensorA.subscribe(distFront)
    simu.Walle.sensorB.subscribe(distSide)

    # PD control

    v = 1 # Just advance

    yu0=0.0  # Initial state of integer for y
    ye0=0.0  # Initial state of error for y
    xe0=0.0  # Initial state of error for y

    # Step variable
    k = 0

    # Initialization
    yui_prev = yu0
    ye_prev = ye0
    xe_prev = xe0

    # Sampling Time
    h=0.1

    # Proportional, integral and derivate constants
    Kp=0.1
    Kpx=0.01
    Ti=10
    Td=1

    # Desired valiues
    yc = -1 # 2.5 meters from wall

    while True:
        # Error between the desired and actual output
        ye = yc - y
        xe = 100 - x

        # Integration Input
        if -100 < yui_prev < 100:
            yui = yui_prev + 1/Ti * h * ye

        # Derivation Input
        yud = 1/Td * (ye - ye_prev)/h

        # Adjust previous values
        ye_prev = ye
        xe_prev = xe
        yui_prev = yui

        # Calculate input for the system
        w = -( Kp * ye + yud)
        w -= Kpx * (xe)


        k += 1
        # if x == 100 and y == 100:
        #     v,w = 1,0
        # print ("PIDy:", str(ye), str(yui), str(yud), "Px:", str(xe))
        # print ("Speed:", str(v), "Angular:", str(w), "X:", str(x), "Y:", str(y))
        motion.publish({"v": v, "w": w})
