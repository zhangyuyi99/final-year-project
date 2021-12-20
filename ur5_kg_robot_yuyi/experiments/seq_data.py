import rtde_control
import rtde_receive
import time
import numpy as np
import kg_robot as kgr
import pygame.midi
from piano import Piano
from note import Note

# all moving distances in meter

# set the finger at central C, at the height of piano key and the wrist flat before running



# def press(note,down_vel,up_vel,distance,hold_time,acc,press_depth):
#
#     ready_position_l = start_position_l[:]
#     ready_position_l[2]+=distance
#     burt.movel(ready_position_l)
#     time.sleep(0.5)
#     # burt.movej(start_position_j)
#     ready_position_j = burt.getj()
#
#     burt.translatel_rel([0, 0, -distance-press_depth, 0, 0, 0], acc=acc, vel = down_vel)
#     time.sleep(hold_time)
#     burt.translatel_rel([0, 0, distance+press_depth, 0, 0, 0], acc=acc, vel = up_vel)
#     time.sleep(0.5)
#
#     return ready_position_l,ready_position_j

# def press(note,down_vel,up_vel,distance,hold_time,acc,press_depth):
#
#
#     ready_position_l = note.position
#     burt.movel(ready_position_l)
#     time.sleep(0.5)
#     # burt.movej(start_position_j)
#
#     # burt.translatel_rel([0, 0, -distance-press_depth, 0, 0, 0], acc=acc, vel = down_vel)
#     # time.sleep(hold_time)
#     # burt.translatel_rel([0, 0, distance+press_depth, 0, 0, 0], acc=acc, vel = up_vel)
#     # time.sleep(0.5)

def move(note):

    ready_position_l = note.position
    burt.movel(ready_position_l)
    time.sleep(2)

tstart = time.time()
burt = kgr.kg_robot(port=30010, db_host="169.254.243.20")

# go to start position every time for caliberation (rigid finger)
start_position_l = [-0.602168, -0.0656458, 0.121373, 2.15931, -2.27794, 0.0549882]
start_position_j = [-0.119586, -1.25544, 2.04127, -2.33096, -1.54294, 3.07975]
burt.movej(start_position_j)
burt.movel(start_position_l)

# set the piano
p = Piano(central_C_position=start_position_l, key_width=[0,0.023,0,0,0,0])

time.sleep(4)
for key, value in p.keys.items():
    move(value)

press_depth_list = np.linspace(0.005,0.015,11)
pygame.midi.init()
device = pygame.midi.Input(1)

# with open('../data/press_depth_exp_acc_2.txt', 'w') as f:
#     output = {'finger_angle': 0, 'down_vel': 0.1, 'up_vel': 0.1, 'distance': 0.10, 'hold_time': 0, 'acc': 2}
#     print(output, file=f)
#     print(output)
#     for press_depth in press_depth_list:
#         for i in range(5):
#             press(down_vel=0.1, up_vel=0.1, distance=0.10, hold_time=0, acc=2, press_depth=press_depth)
#             event = device.read(2)
#             output = {'press_depth': press_depth, 'midi': event}
#             print(output, file=f)
#             print(output)

burt.movel(start_position_l)









