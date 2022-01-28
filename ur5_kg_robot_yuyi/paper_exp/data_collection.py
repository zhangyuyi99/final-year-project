# soft finger pre
# set the finger at la, at the height of piano key and the wrist flat before running

import time
import numpy as np
import ur5_kg_robot_yuyi.kg_robot as kgr
import pygame.midi

vel_list = np.linspace(0.001,0.008,15)
acc_list = np.array([0.1,0.5,1.0])
distance = 0.05
depth_list = np.array([0.002,0.003,0.004])
hold_time = 0
# stiffness [0,-20,-40,-60,-80] kPa
# data points: 5*20*3*3*3 = 2700 in total

# manual:
stiffness = 0
angle = 0


def press(vel,distance,hold_time,press_depth,acc):

    ready_position_l = start_position_l[:]
    ready_position_l[2]+=distance
    burt.movel(ready_position_l)
    time.sleep(0.5)
    # burt.movej(start_position_j)
    ready_position_j = burt.getj()

    burt.translatel_rel([0, 0, -distance-press_depth, 0, 0, 0], acc=acc, vel = vel)
    time.sleep(hold_time)
    burt.translatel_rel([0, 0, distance+press_depth, 0, 0, 0], acc=acc, vel = vel)
    time.sleep(0.5)


tstart = time.time()
burt = kgr.kg_robot(port=30010, db_host="169.254.1.1")

start_position_l = burt.getl()
print(start_position_l)
key_height = start_position_l[2]


pygame.midi.init()
device = pygame.midi.Input(1)

with open('paper_data/soft_0_angle_0.txt', 'a') as f:

    # vel_list = np.linspace(0.001, 0.008, 15)
    # acc_list = np.array([0.1, 0.5, 1.0])
    # distance = 0.05
    # press_depth = np.array([0.002, 0.003, 0.004])
    # hold_time = 0

    for acc in acc_list:
        for vel in vel_list:
            for depth in depth_list:

                control_param = [stiffness,angle,acc,vel,depth,distance,hold_time]

                press(vel=vel,distance=distance,hold_time=hold_time,press_depth=depth,acc=acc)

                # midi format: [velocity] = 1~60 (Max possible 127)
                event = device.read(2)
                output = {'control':control_param, 'midi': event}
                print(output, file=f)
                print(output)




