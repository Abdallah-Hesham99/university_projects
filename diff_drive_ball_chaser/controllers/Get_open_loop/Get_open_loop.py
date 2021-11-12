"""Get_open_loop controller."""# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot,Keyboard
import math
import matplotlib.pyplot as plt
import numpy as np


# create the Robot instance.
robot = Robot()
keyboard = Keyboard()

# get the time step of the current world.
timestep = 64
max_sped=6.2
keyboard.enable(timestep)
ds_sens = {}

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)
motor1 = robot.getDevice('left_motor')
motor2 = robot.getDevice('right_motor')
ds = robot.getDevice('center_ds')
cam = robot.getDevice('camera')
cam.enable(timestep)
ds_sens['left_ds'] = robot.getDevice('left_ds')
ds_sens['center_ds'] = robot.getDevice('center_ds')
ds_sens['right_ds'] = robot.getDevice('right_ds')
for i,j in ds_sens.items():
    j.enable(timestep)
    
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
L = 0.14
positions  =[]
pids = []
counter = 4
from simple_pid import PID
pid = PID(2, 0.001, 0.012, setpoint=0)
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    
    setpoint = 0
    ds_reading = [ds.getValue() for key, ds in ds_sens.items()]
    print('ds readings are {}'.format(ds_reading))
    
       
    if ds_reading[1]<1000:
        pid.setpoint -=math.pi/2
     
    if ds_reading[0]<1000:
        pid.setpoint -=0.1
    
 
    if ds_reading[2]<1000:
  
        pid.setpoint -= -0.1
    if ds_reading[0]<1000 and ds_reading[1]<1000 and ds_reading[2]<1000:
         pid.setpoint -=math.pi * 0.25
        # left_sped = 0.1*max_sped
         #right_sped = 0.1*max_sped
         #motor1.setVelocity(left_sped)
         #motor2.setVelocity(right_sped) 
   
  

   
   
   
   
    
    for i in range(2):
        encoder_values[i] = encoder_list[i].getValue()
        
        diff[i] = encoder_values[i] - last_encoder_value[i]
        #print(diff)
        
        distances[i] = diff[i] * circum / 6.28 
    v = (distances[0] + distances[1])/2.0
    w = (distances[1] - distances[0])/L 
    
    
    dt =0.85
    robot_pose[2] += w*dt
    vx = v *math.cos(robot_pose[2])
    vy = v *math.sin(robot_pose[2])

    robot_pose[0] += vx *dt        
    robot_pose[1] += vy *dt        
    
  #  if abs(robot_pose[2])>=2*math.pi+0.0001:
        
   #     robot_pose[2] = 0
        
    
    print('robot_pose : {}'.format(robot_pose))
    
    # Process sensor data here.
    
    
    
    
    
    right_sped=0.0*max_sped
    left_sped=0.0*max_sped
    key=keyboard.getKey()
    
    
    if (key==ord('O')):
  
        
        right_sped=0.2*max_sped
        left_sped=0.2*max_sped
        
    if (key==ord('L')):
        right_sped=0.2*max_sped
        left_sped=0*max_sped       
        
    if (key==ord('K')):
        right_sped=-0.2*max_sped
        left_sped=-0.2*max_sped       
        
    
    if (key==ord('M')):
        right_sped=0*max_sped
        left_sped=0.2*max_sped       
         
    
    
    if (key==ord('B')):
  
        
        pid.setpoint =1.5
        
    if (key==ord('C')):
        pid.setpoint =0       
        
    if (key==ord('D')):
        pid.setpoint =3.14    
        
    
    if (key==ord('R')):
        
        pid.setpoint +=-0.1
    
          
    
    print('phi is {}'.format(robot_pose[2]))
    if pid.setpoint>2.5*math.pi:
        pid.setpoint = 2.5*math.pi
    if pid.setpoint<-2.5*math.pi:
        pid.setpoint = -2.5*math.pi
    pid.output_limits = (-7,7)
    
 #   pid.setpoint = 3.14 if c >20 else 0
#    out = pid(robot_pose[2])
    error = robot_pose[2] - pid.setpoint
    out = 0
    #print('El value Yasta ! {}'.format(out))
    print('out is {}, Fuzzy setpoint is {}'.format(out,pid.setpoint))
    left_sped += ((2 * v) + (pid.setpoint * L)) / (2 * wheel_radius)
    right_sped += ((2 * v) - (pid.setpoint * L)) / (2 * wheel_radius)

    motor1.setVelocity(left_sped)
    motor2.setVelocity(right_sped)
   
   
   
   
   
#    c += 1
   
   
    positions.append(robot_pose[2])
    pids.append(pid.setpoint)
    if (key==ord('Y')):
    
        plt.plot(pids,'-r')
        plt.plot(positions, 'g--')
        num_path = 'D:\My_files\Learning\Webots\Trial\Trial\pid3_data.npy'
        pth = 'D:\My_files\Learning\Webots\Trial\Trial\Photos\Fuzzy_control_' + str(counter) +'.png'
        set_path = 'D:\My_files\Learning\Webots\Trial\Trial\data\setpoint_data.npy'
        plt.savefig(pth)
      #  np.save(num_path,positions)
       # np.save(set_path,pids)
      #  plt.title('fuzz')
#       pid.Kd +=0.005
        counter +=1
    
    for i in range(2):
       last_encoder_value[i] = encoder_values[i]
    

# Enter here exit cleanup code.
#pth = 'D:\My_files\Learning\Webots\Trial\Trial\Photos\fuzzy_' + str(counter) +'.png'
plt.plot(pids,'-r')
plt.plot(positions, 'g--')



import scipy.io


scipy.io.savemat('data4.mat', dict(x=pids, y=positions))
#plt.savefig(pth)
plt.show()

#cv2.waitKey(0)
#cv2.destroyAllWindows()
