import numpy as np
import matplotlib.pyplot as plt

pid = np.load('pid_data.npy')
set1 = np.load('setpoint_data.npy')
plt.plot(pid)
plt.plot(set1)
plt.legend(['PID','Setpoint'])
plt.title('responese (setpoint = 3.14 rad) ')
plt.show()
