from math import pi

# home position
# positions generally in [x,y,z,rx,ry,rz] = [[cartesian]/mm,[axis angle]/rad]
# positions terminating in j correspond to joint angles/rad
burt_homej = [-1.57255, -1.29794, -1.18718, -2.22769, 1.57521, -0.00545246]
# burt_homej = [-0.382069, -0.056534, 0.142337, 2.22913, 2.17051, -0.0308429]
# gripper tool centre points (tcp)
no_gripper_tcp = [0,0,0,0,0,0]
lego_tcp = [0,0,0.041,0,0,0]