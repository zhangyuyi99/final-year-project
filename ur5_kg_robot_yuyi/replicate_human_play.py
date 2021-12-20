# rigid finger
import scipy.io
import numpy as np
import time
import kg_robot as kgr
import pygame.midi

def read_play_file(filename):
    file = filename
    mat = scipy.io.loadmat(file)

    down_vel_list = 0.001*np.array(mat['down_vel_list'])[0]
    print(down_vel_list)

    up_vel_list = 0.001*np.array(mat['up_vel_list'])[0]
    print(up_vel_list)

    note_list = np.array(mat['note_list'])[0]
    note_list = [3,2,1,2,3,3,3,2,2,2,3,5,5]
    print(note_list)

    hold_time_list = np.array(mat['hold_time_list'])[0]
    print(hold_time_list)

    play_data = {'note_list':note_list, 'down_vel_list':down_vel_list, 'up_vel_list':up_vel_list, 'note_list':note_list, 'hold_time_list':hold_time_list}

    return play_data
# down_vel_list
# up_vel_list
# note_list
# hold_time_list
# down_time_list
# up_time_list

def press(start_position_l, note,down_vel,up_vel,hold_time=0.5,acc=0.5, iflast=False):
    distance = down_vel**2/(2*acc)+0.05
    ready_position_l = start_position_l[:]
    ready_position_l[1] += (note - 1) * key_width
    ready_position_l[2]+=distance
    burt.movel(ready_position_l, acc = acc)
    # burt.movej(start_position_j)
    ready_position_j = burt.getj()

    burt.translatel_rel([0, 0, -distance-0.015, 0, 0, 0], acc=acc, vel=down_vel)
    time.sleep(hold_time)

    if iflast:
        burt.translatel_rel([0, 0, 0.015, 0, 0, 0], acc=acc, vel=up_vel)

def play(start_position_l, play_data):

    for i in range(len(play_data['note_list'])):
        note = play_data['note_list'][i]
        down_vel = play_data['down_vel_list'][i]
        up_vel = play_data['up_vel_list'][i]
        hold_time = play_data['hold_time_list'][i]
        if isinstance(note,int) and note>0:
            # ready_position = start_position_l[:]
            # # ready_position[1] += (note-1)*key_width
            # # # ready_position[2] += distance
            # burt.movel(ready_position)
            iflast = (i==len(play_data['note_list'])-1)
            press(start_position_l = start_position_l, note = note, down_vel=down_vel,up_vel=up_vel,hold_time=hold_time, acc=0.5,iflast=iflast)
        elif note==0:
            time.sleep(2)



key_width = 0.024
tstart = time.time()
burt = kgr.kg_robot(port=30010, db_host="169.254.1.1")
time.sleep(6)
start_position_l = burt.getl()
play_data = read_play_file('play_data/rigid_play_data.mat')
print(play_data)
play(start_position_l, play_data)

burt.movel(start_position_l)