# soft finger pre
# set the finger at la, at the height of piano key and the wrist flat before running
import time
import numpy as np
import kg_robot as kgr
import pygame.midi

vel_list = np.linspace(0.01,0.08,15)
# acc_list = np.array([0.1,0.5,1.0])
acc_list = 0.1
distance = 0.05
# depth_list = np.array([0.02,0.03,0.04])
depth_list = 0.02
hold_time = 0
# stiffness [0,-20,-40,-60,-80] kPa
# data points: 5*20*3*3*3 = 2700 in total

# manual:
stiffness = 0
angle = 0




tstart = time.time()
burt = kgr.kg_robot(port=30010, db_host="169.254.243.20")
print(burt.getl())

