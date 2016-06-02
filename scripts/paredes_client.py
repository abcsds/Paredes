#! /usr/bin/env python3
"""
Test client for the <paredes> simulation environment.

This simple program shows how to control a robot from Python.

For real applications, you may want to rely on a full middleware,
like ROS (www.ros.org).
"""

import sys
# import numpy as np

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
    global x
    if sensor['point_list'][5][0] == 0:
        x = 100
    else:
        x = sensor['point_list'][5][0]
        x = x - 2.5 # Offset for the integral

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

    # PID control

    xu0=0.0  # Initial state of integer for x
    yu0=0.0  # Initial state of integer for y

    xe0=0.0  # Initial state of error for x
    ye0=0.0  # Initial state of error for y

    # Step variable
    k = 0

    # Initialization
    xui_prev = xu0
    yui_prev = yu0
    xe_prev = xe0
    ye_prev = ye0

    # Sampling Time
    h=0.1

    # Proportional, integral and derivate constants
    Kp=0.1
    Ti=100
    Td=100

    # Desired valiues
    xc = 100
    yc = 0 # 2.5 meters from wall

    # while True: # Get to a wall
    #     if x > 2.5:
    #         v = 1
    #         motion.publish({"v": v, "w": w})
    #     else:
    #         v = 0
    #         motion.publish({"v": v, "w": w})
    #         break

    while True:
        # Error between the desired and actual output
        xe = xc - x
        ye = yc - y

        # Integration Input
        if -100 < xui_prev < 100:
            xui = xui_prev + 1/Ti * h * xe
        if -100 < yui_prev < 100:
            yui = yui_prev + 1/Ti * h * ye

        # Derivation Input
        xud = 1/Td * (xe - xe_prev)/h
        yud = 1/Td * (ye - ye_prev)/h

        # Adjust previous values
        xe_prev = xe
        ye_prev = ye
        xui_prev = xui
        yui_prev = yui

        # Calculate input for the system
        # v = Kp * xe + xui + xud
        # v = Kp * xe + xud
        v = Kp * (xe)
        # w = Kp * ye + yui + yud
        # w = Kp * ye + yud
        w = -( Kp * (ye) )

        k += 1
        v += 0.5
        print ("PIDx:", str(xe), str(xui), str(xud), "PIDy:", str(ye), str(yui), str(yud))
        print ("Speed:", str(v), "Angular:", str(w), "X:", str(x), "Y:", str(y))
        motion.publish({"v": v, "w": w})
