
# set the finger at central C, at the height of piano key and the wrist flat before running
import operator
import time
import kg_robot as kgr
import pygame.midi

class Style:
  def __init__(self, name, distance=0.2, down_vel=1, down_acc=1, up_vel=1, up_acc=1, hold_time=0.5, finger_angel=0):
    self.name = name
    # at key: z = -0.265m, CONTROL PARAMETERS ARE IN METERS!!
    self.distance = distance  #vertical distance from piano key
    self.down_vel = down_vel
    self.down_acc = down_acc
    self.up_vel = up_vel
    self.up_acc = up_acc
    self.hold_time = hold_time
    self.finger_angel = finger_angel

## UR5 info: max_speed 1m/s
# styles
# distance, down_vel, down_acc, up_vel, up_acc, hold_time, finger_angel
metal = Style("metal", 0.2, 2, 3, 2, 3, 1, 0) # large stiffness
gentle = Style("gentle", distance=0.00, down_vel=0.5, up_vel=0.02,hold_time=0.5)
power = Style("power", distance=0.2, down_vel=0.5, up_vel=0.5, hold_time=1.5)
flow = Style("flow", distance=0.05, up_vel=0.5, hold_time=0.3)
bump = Style("bump", distance=0.00, down_vel=2, up_vel=2, hold_time=0.3)
drama = Style("drama", distance=0.2, down_vel=5, up_vel=5, hold_time=0.1)
beat = Style("beat", distance=0.05, down_vel=2, up_vel=2, hold_time=0.1)

style_list = [metal, gentle, power, flow, bump, drama, beat]

key_width = 0.025 # 2.2cm

def press(style):
    burt.translatel_rel([0, 0, -style.distance-0.015, 0, 0, 0], style.down_acc, style.down_vel)
    time.sleep(style.hold_time)
    burt.translatel_rel([0, 0, style.distance+0.015, 0, 0, 0],style.up_acc, style.up_vel)
    time.sleep(0)

# [-0.273755, -0.0312353, 0.177908, 1.31198, 2.67658, 0.100856]
# [-0.27372, -0.031241, 0.1779, 0.906258, 2.75774, 0.170274]

glissando_ready = [-0.444017, -0.0108752, 0.153406, 0.975774, 2.76666, 0.159331]
onkey_press_ready = [-0.42221, -0.0216074, 0.122206, -1.41156, -2.80334, -0.0159958]

def glissando(start_position, direction = 'right', key_number = 7, speed=1):
    # get gesture ready
    burt.translatel_rel(list(map(operator.sub, glissando_ready, onkey_press_ready)))
    # burt.rotate_rel(list(map(operator.sub, onkey_press_ready, glissando_ready)))
    time.sleep(3)
    # burt.rotate_rel(list(map(operator.sub, glissando_ready, onkey_press_ready)))
    burt.translatel_rel(list(map(operator.sub, onkey_press_ready, glissando_ready)))


def play(start_position ,notes, style, speed=1):

    for note in notes:
        if isinstance(note,int) and note>0:
            ready_position = start_position[:]
            ready_position[1] += (note-1)*key_width
            ready_position[2] += style.distance
            burt.movel(ready_position)
            press(style)
        elif note==0:
            time.sleep(2)




tstart = time.time()
burt = kgr.kg_robot(port=30010, db_host="169.254.1.1")
# burt.movel(onkey_press_ready)
start_position = burt.getl()
print(start_position)
key_height = start_position[2]

# pygame.midi.init()
# device = pygame.midi.Input(1)


# style showing
# for style in style_list:
#     ready_position = start_position[:]
#     ready_position[2]+=style.distance
#     burt.movel(ready_position)
#     press(style)
#     time.sleep(0)
#     # midi format: [[status, note, velocity, 0], timestamp]
#     # status: 144-on, 128-off
#     event = device.read(2)
#     print(event)
#
# burt.movel(start_position)
# print(burt.getl())

# music demo playing
# music = [3,2,1,2,3,3,3,0,2,2,2,0,3,3,3,0,3,2,1,2,3,3,3,0,2,2,3,2,1]
#
# music_2 = [1,2,3,4,5,6,7,8]
# time.sleep(10)
# play(start_position, music_2, gentle)

# burt.movel([-0.446594, 0.0192894, 0.157076, 1.31198, 2.67658, 0.100856])
print(burt.getl())
print(burt.getj())
# glissando(start_position)

# ## finger angle 0
# angel_0_l = [-0.491896, -0.133811, 0.162229, 2.19036, -1.79967, -0.377479]
# angel_0_r = [-0.0421799, -1.39079, 2.39143, -2.95204, -1.50447, 2.9228]
#
# ## finger angle 90
# angel_90_l = [-0.557448, -0.136604, 0.207133, -2.00122, 1.69204, -0.782536]
# angel_90_r = [-0.0228699, -1.33616, 1.62356, -1.15319, -1.53004, 2.93729]
#
# ## updated 09/11/2021 by yuyi
# ## finger angle 0
# angel_0_l = [-0.491896, -0.133811, 0.162229, 2.19036, -1.79967, -0.377479]
# angel_0_r = [-0.0421799, -1.39079, 2.39143, -2.95204, -1.50447, 2.9228]
#
# ## finger angle 90
# angel_90_l = [-0.557448, -0.136604, 0.207133, -2.00122, 1.69204, -0.782536]
# angel_90_r = [-0.0228699, -1.33616, 1.62356, -1.15319, -1.53004, 2.93729]

## updated 10/11/2021 by yuyi
## finger angle 0
angel_0_l =[-0.503357, -0.138393, 0.148142, 1.93366, -1.84498, -0.657536]
angel_0_j = [0.0205327, -1.17986, 2.38127, -3.38711, -1.62635, 3.10386]

## finger angle 90
angel_90_l = [-0.562234, -0.129058, 0.196366, -2.00268, 1.69174, -0.784557]
angel_90_j = [-0.036846, -1.32076, 1.63276, -1.17739, -1.53747, 2.92534]


burt.movel(angel_90_l)
burt.movej(angel_90_j)

#
one_step_l = [(i - j)/3 for i, j in zip(angel_90_l, angel_0_l)]
one_step_j = [(i - j)/3 for i, j in zip(angel_90_j, angel_0_j)]


#
# for i in range(4):
#     print(i)
#     burt.translatel_rel(one_step_l)
#     burt.movej_rel(one_step_j)
#     time.sleep(1)

# burt.movej(angel_0_j)
# burt.movel(angel_0_l)
#
# # burt.translatel_rel([0, key_width*4, 0, 0, 0, 0],go_acc, go_velo)
# # burt.movel([-0.335845, 0.0547358-3*0.024, 0.180464, 1.27118, 2.84003, 0.111631],0.05, 0.05)
#
# burt.close()


