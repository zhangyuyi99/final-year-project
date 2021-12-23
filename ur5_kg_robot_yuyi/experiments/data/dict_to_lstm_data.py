import ast
import numpy as np
import torch
# data preprocessing and convert to torch tensor


def note_to_num(note_name):
    num = int(ord(note_name)-66)
    if num > 0:
        return num
    else:
        return num+7

# Input shape: (1, 1, 5) = (batch size, sequence length, feature number)

with open('seq_data.txt', 'r') as f:
    lines = f.readlines()
    ctrl = np.zeros((100,12,10), dtype=float)
    midi = np.zeros((100,12,5), dtype=int)
    current_group = 0
    current_sequence = np.zeros((1, 12, 10), dtype=float)
    for line in lines:
        dict = ast.literal_eval(line)
        l = list(dict.values())
        l[2] = note_to_num(l[2])
        print(l)
        ctrl[l[0]][l[1]] = np.asarray(l[2:-1])
        # 'midi': [[[144, 69, 54, 0], 28854], [[128, 69, 86, 0], 29480]] --> [69, 54, 28854, 86, 29480] = [note, down_vel, down_time, up_vel, up_time]
        current_midi = l[-1]
        if current_midi != []:
            midi[l[0]][l[1]] = [current_midi[0][0][1], current_midi[0][0][2], current_midi[0][1], current_midi[1][0][2], current_midi[1][1]]
        # print(ctrl[l[0]][l[1]])
        # print(midi[l[0]][l[1]])




    # ctrl[ctrl != np.array(None)]
    # midi[midi != np.array(None)]
    print(ctrl)
    print(midi)



    # s = f.read()
