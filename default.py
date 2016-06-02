#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <paredes> environment

Feel free to edit this template as you like!
"""

from morse.builder import *

# Add the MORSE mascott, MORSY.
# Out-the-box available robots are listed here:
# http://www.openrobots.org/morse/doc/stable/components_library.html
#
# 'morse add robot <name> paredes' can help you to build custom robots.
robot = Pioneer3DX()

# The list of the main methods to manipulate your components
# is here: http://www.openrobots.org/morse/doc/stable/user/builder_overview.html
# robot.translate(1.0, 0.0, 0.0)
# robot.rotate(0.0, 0.0, 3.5)

# Add a motion controller
# Check here the other available actuators:
# http://www.openrobots.org/morse/doc/stable/components_library.html#actuators
#
# 'morse add actuator <name> paredes' can help you with the creation of a custom
# actuator.
# motion = MotionVW()
motion = MotionVWDiff()
robot.append(motion)

# stop()
# Stop the robot
#
# Internally, it sets (v, w) to (0.0, 0.0)
#
# set_speed(v, w)
# Modifies v and w according to the parameters
#
# Parameters
# v: desired linear velocity (meter by second)
# w: desired angular velocity (radian by second)


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

# Add a keyboard controller to move the robot with arrow keys.
# keyboard = Keyboard()
# robot.append(keyboard)
# keyboard.properties(ControlType = 'Position')

# Add a pose sensor that exports the current location and orientation
# of the robot in the world frame
# Check here the other available actuators:
# http://www.openrobots.org/morse/doc/stable/components_library.html#sensors
#
# 'morse add sensor <name> paredes' can help you with the creation of a custom
# sensor.
pose = Pose()
robot.append(pose)

# Name
robot.name = "Walle"
#=> robot.name

# To ease development and debugging, we add a socket interface to our robot.
#
# Check here: http://www.openrobots.org/morse/doc/stable/user/integration.html
# the other available interfaces (like ROS, YARP...)
robot.add_default_interface('socket')


# set 'fastmode' to True to switch to wireframe mode
# env = Environment('sandbox', fastmode = False)
# env = Environment('indoors-1/boxes')
env = Environment('indoors-1/maze')
# env = Environment('indoors-1/room')
# env.set_camera_location([-18.0, -6.7, 10.8])
# env.set_camera_rotation([1.09, 0, -1.14])

# import statistics as stats

# print(stats.mean(sensorA.point_list))
