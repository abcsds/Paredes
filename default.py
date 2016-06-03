#! /usr/bin/env morseexec

from morse.builder import *

robot = Pioneer3DX()
motion = MotionVWDiff()
robot.append(motion)

# Append a sensor A
sensorA = SickLDMRS()
sensorA.properties(Visible_arc = True)
sensorA.properties(resolution = 1.0)
sensorA.properties(scan_window = 10)
sensorA.properties(laser_range = 5.0)
sensorA.properties(layers = 1)
sensorA.properties(layer_separation = 0.8)
sensorA.properties(layer_offset = 0.25)
sensorA.translate(x=.2,z=.2)
robot.append(sensorA)

# Append a sensor B
sensorB = SickLDMRS()
sensorB.properties(Visible_arc = True)
sensorB.properties(resolution = 1.0)
sensorB.properties(scan_window = 10)
sensorB.properties(laser_range = 5.0)
sensorB.properties(layers = 1)
sensorB.properties(layer_separation = 0.8)
sensorB.properties(layer_offset = 0.25)
sensorB.translate(y=.1, z=0.2)
sensorB.rotate(z=3.1416/2)
robot.append(sensorB)

pose = Pose()
robot.append(pose)

# Name
robot.name = "Walle"

robot.add_default_interface('socket')


# set 'fastmode' to True to switch to wireframe mode
# env = Environment('sandbox', fastmode = False)
# env = Environment('indoors-1/boxes')
env = Environment('indoors-1/maze', fastmode = True)
# env = Environment('indoors-1/room')
