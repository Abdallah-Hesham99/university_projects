import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl 

error = ctrl.Antecedent(np.arange(-2*np.pi,2*np.pi), 'error')
phi_ = ctrl.Consequent(np.arange(-2*np.pi,2*np.pi),'phi_')


phi_['poor'] = fuzz.trimf(phi_.universe, [-8, -6,-3 ])
phi_['mediocre'] = fuzz.trimf(phi_.universe, [-4, -2, 0])
phi_['average'] = fuzz.trimf(phi_.universe, [-2, 0, 2])


phi_['decent'] = fuzz.trimf(phi_.universe, [0, 2,4 ])
phi_['good'] = fuzz.trimf(phi_.universe, [3, 6, 8])

error['poor'] = fuzz.trimf(error.universe, [-8, -6,-3 ])
error['mediocre'] = fuzz.trimf(error.universe, [-4, -2, 0])
error['average'] = fuzz.trimf(error.universe, [-2, 0, 2])


error['decent'] = fuzz.trimf(error.universe, [0, 2,4 ])
error['good'] = fuzz.trimf(error.universe, [3, 6, 8])



#rule1 = ctrl.Rule(error['dismal'], phi_['excellent'])
rule2 = ctrl.Rule(error['poor'], phi_['good'])
rule3 = ctrl.Rule(error['mediocre'], phi_['decent'])
rule4 = ctrl.Rule(error['average'], phi_['average'])
rule5 = ctrl.Rule(error['decent'], phi_['mediocre'])
rule6 = ctrl.Rule(error['poor'], phi_['good'])
#rule7 = ctrl.Rule(error['excellent'], phi_['dismal'])
phi_ctrl = ctrl.ControlSystem( [rule2, rule3,rule4,rule5,rule6])
phi =  ctrl.ControlSystemSimulation(phi_ctrl)
phi.input['error'] = -6.5



def get_value(err):
	Gain = 1
	phi.input['error']  = err
	phi.compute()
	return phi.output['phi_'] * Gain

