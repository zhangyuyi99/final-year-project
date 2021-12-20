"""
    Uses Kieran's client
    Called from Matlab with 2 variables
"""

import time
from typing import Any, Union

import numpy as np
import serial
import math
from math import pi
import socket
import sys
import sched
import waypoints as wp
import kg_robot as kgr

tstart = time.time()

ip_add = "169.254.1.1"  # change this to your ip address
# ip_add = "10.0.2.15"  # change this to your ip address

burt = kgr.kg_robot(port=30010,db_host=ip_add)
burt.movel([-0.182069, 0.1-0.056534, 0.102337, 2.22913, 2.17051, -0.0308429],0.05, 0.05)
for i in range(2):
    burt.translatel_rel([0, 0, -0.04, 0, 0, 0],0.05, 0.05)
    time.sleep(1)
    burt.translatel_rel([0, 0, 0.04, 0, 0, 0],0.05, 0.05)
    time.sleep(3)

burt.movel([-0.182069, 0.1-0.056534, 0.102337, 2.0102, 1.961, -0.41],0.05, 0.05)
for i in range(2):
    burt.translatel_rel([0, 0, -0.04, 0, 0, 0], 0.05, 0.05)
    time.sleep(1)
    burt.translatel_rel([0, 0, 0.04, 0, 0, 0], 0.05, 0.05)
    time.sleep(3)

burt.movel([-0.182069, 0.1-0.056534, 0.102337, 1.7, 1.66, -0.79],0.05, 0.05)
for i in range(2):
    burt.translatel_rel([0, 0, -0.04, 0, 0, 0], 0.05, 0.05)
    time.sleep(1)
    burt.translatel_rel([0, 0, 0.04, 0, 0, 0], 0.05, 0.05)
    time.sleep(3)

burt.movel([-0.182069, 0.1-0.056534, 0.102337, 1.28, 1.259, -1.14],0.05, 0.05)
for i in range(2):
    burt.translatel_rel([0, 0, -0.04, 0, 0, 0], 0.05, 0.05)
    time.sleep(1)
    burt.translatel_rel([0, 0, 0.04, 0, 0, 0], 0.05, 0.05)
    time.sleep(3)

burt.movel([-0.182069, 0.1-0.056534, 0.102337, 2.22913, 2.17051, -0.0308429],0.05, 0.05)

# rtangle = np.deg2rad([0, 0, 0, 0, 30, 0])
# #first down
# burt.translatel_rel([0, 0, -0.01, 0, 0, 0], 0.05, 0.2)  # move up for time defined in matlab
# burt.translatel_rel([0, 0, 0.01, 0, 0, 0], 0.05, 0.2)
# burt.movej_rel(rtangle)
# #second down
# burt.translatel_rel([0, 0, -0.1, 0, 0, 0], 0.5, 0.02)
# burt.translatel_rel([0, 0, 0.1, 0, 0, 0], 0.5, 0.02)
# burt.movej_rel(rtangle)
# # third down
# burt.translatel_rel([0, 0, -0.1, 0, 0, 0], 0.5, 0.02)
# burt.translatel_rel([0, 0, 0.1, 0, 0, 0], 0.5, 0.02)
# burt.movej_rel(rtangle)
# # fourth down
# burt.translatel_rel([0, 0, -0.1, 0, 0, 0], 0.5, 0.02)
# burt.translatel_rel([0, 0, 0.1, 0, 0, 0], 0.5, 0.02)
#
# burt.home()
# start_time = time.time()
# while time.time() - start_time < 50:
#     x = -0.055 * np.sin(2*time.time())
#     y = -0.055 * np.cos(2*time.time())
#     burt.translatel_rel([x, y, 0, 0, 0, 0], 0.5, 0.02)


print(burt.getl())



# Below is a bare bones example of how the rest of the script used servoj to regularly call a function
# I haven't tested it on a UR5 so there could be typos!

# # scheduler used to regularly pass desired positions to servoj
# scheduler = sched.scheduler(time.time, time.sleep)
#
# def schedule_it(dt, duration, callable, *args):
#     for i in range(int(duration / dt)):
#         scheduler.enter(i * dt, 1, callable, args)
#
# # main function: moves upwards in time (but could be used to set any desired position)
# def parameter_move(startingpose, t0):
#     t = time.time() - t0
#     burt.servoj(startingpose + [0, 0, 0.01 * t, 0, 0, 0], vel=50, control_time=0.05)
#
# t0 = time.time()
# startingpose = burt.getl()
# # schedule UR5 to move upwards slowly by calling parameter_move every 0.05s for 5s
# schedule_it(0.05, 5, parameter_move, startingpose, t0)
#
# # run scheduler calling servoj
# scheduler.run()

burt.close()

