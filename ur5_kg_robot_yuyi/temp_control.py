import time
import serial
import math
from math import pi
import numpy
import socket
import sys
import sched
import waypoints as wp
import kg_robot as kgr

tstart = time.time()
# 这个代码不好用，别用！！！！一直连接不上， whj 20210716
burt = kgr.kg_robot(port=30010, db_host="169.254.1.1")

print(burt.getl())
burt.movel([-0.371539, 0.0395437, 0.176586, -1.28938, -2.69125, -0.395747],0.05, 0.05)

# burt.movel([-0.371524, 0.0395449, 0.177017, -1.3036, -2.77515, -0.475064],0.05, 0.05)