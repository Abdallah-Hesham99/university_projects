"""drive_with_position controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot,Keyboard
import math
# create the Robot instance.
robot = Robot()
keyboard = Keyboard()

# get the time step of the current world.
timestep = 64
max_sped=6.2
keyboard.enable(timestep)
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
encoder_1 = robot.getDevice('ps1')
encoder_2 = robot.getDevice('ps2')
encoder_1.enable(timestep)
encoder_2.enable(timestep)
encoder_list = [encoder_1,encoder_2]
motor1.setPosition(float('inf'))
motor2.setPosition(float('inf'))
motor1.setVelocity(0.0)
motor2.setVelocity(0.0)
encoder_values = [0,0]
wheel_radius = 0.0325
circum = 2 * math.pi*wheel_radius
distances =[0,0]


robot_pose = [0,0,0] # x,y,phi
last_encoder_value =[0,0]
diff=[0,0]
L = 1.1
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    left_sped = 0.1*max_sped
    right_sped = 0.1*max_sped
    distance = ds.getValue()
    for i in range(2):
        encoder_values[i] = encoder_list[i].getValue()
        
        diff[i] = encoder_values[i] - last_encoder_value[i]
        #print(diff)
        
        distances[i] = diff[i] * circum / 6.28 
    v = (distances[0] + distances[1])/2.0
    w = (distances[1] - distances[0])/L 
    
    
    dt =1
    robot_pose[2] += w*dt
    vx = v *math.cos(robot_pose[2])
    vy = v *math.sin(robot_pose[2])

    robot_pose[0] += vx *dt        
    robot_pose[1] += vy *dt        
    
    if abs(robot_pose[2])>=2:
        
        robot_pose[2] = 0
    
    print('robot_pose : {}'.format(robot_pose))
    
    # Process sensor data here.
    
    
    
  
    right_sped=0.1*max_sped
    left_sped=0.1*max_sped
    key=keyboard.getKey()
    if (key==ord('B')):
  
        right_sped=0.1*max_sped
        left_sped=0.1*max_sped
     
        
    if (key==ord('C')):
        right_sped=0.1*max_sped
        left_sped=0*max_sped
        
    if (key==ord('D')):
        right_sped=0*max_sped
        left_sped=0.1*max_sped
        
    
    if (key==ord('R')):
        right_sped=-0.1*max_sped
        left_sped=-0.1*max_sped
        
        
     
    motor1.setVelocity(left_sped)
    motor2.setVelocity(right_sped)
    """
    if distance<1000:
        right_sped=0.4*max_sped
        left_sped=0
  
    else:
        left_sped=0.2*max_sped
        right_sped=0
    motor1.setVelocity(left_sped)
    motor2.setVelocity(right_sped)
    """
    for i in range(2):
       last_encoder_value[i] = encoder_values[i]
    

# Enter here exit cleanup code.
