"""drive controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
import numpy as np
#import gym 
# create the Robot instance.
robot = Robot()


# get the time step of the current world.
timestep = 64
max_sped=6.2
# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)
motor1 = robot.getDevice('left_motor')
motor2 = robot.getDevice('right_motor')
ds = robot.getDevice('diss')
cam = robot.getDevice('camera')
cam.enable(timestep)
ds.enable(timestep)
motor1.setPosition(float('inf'))
motor2.setPosition(float('inf'))


motor1.setVelocity(0.0)
motor2.setVelocity(0.0)



# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    left_sped = 0.5*max_sped
    right_sped = 0.5*max_sped
    distance = ds.getValue() 
    photo = np.array(cam.getImageArray())
    print(photo.shape)
    # Process sensor data here.
    motor1.setVelocity(left_sped)
    motor2.setVelocity(right_sped)
    if distance<950:
        right_sped=0.3*max_sped
        left_sped=0
    else:
        right_sped=0.3*max_sped
        left_sped=0.3*max_sped
    motor1.setVelocity(left_sped)
    motor2.setVelocity(right_sped)
    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
