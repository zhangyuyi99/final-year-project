import torch
import torch.nn as nn

# {'group': 0, 'order': 11, 'note', 'move_vel', 'down_vel', 'up_vel', 'distance', 'hold_time', 'move_acc', 'down_acc', 'up_acc', 'press_depth', 'midi': [[[144, 69, 54, 0], 28854], [[128, 69, 86, 0], 29480]]}
input_dim = 5 # 'midi': [[[144, 69, 54, 0], 28854], [[128, 69, 86, 0], 29480]] --> [69, 28854, 86, 29480] = [down_vel, down_time, up_vel, up_time]
hidden_dim = 10 # 'note', 'move_vel', 'down_vel', 'up_vel', 'distance', 'hold_time', 'move_acc', 'down_acc', 'up_acc', 'press_depth'
n_layers = 1

lstm_layer = nn.LSTM(input_dim, hidden_dim, n_layers, batch_first=True)

batch_size = 1
seq_len = 3

input = torch.randn(batch_size, seq_len, input_dim)
hidden_state = torch.randn(n_layers, batch_size, hidden_dim)
cell_state = torch.randn(n_layers, batch_size, hidden_dim)
hidden = (hidden_state, cell_state)

out, hidden = lstm_layer(input, hidden)
print("Input shape: ", input.shape)
print("Output shape: ", out.shape)
print("Hidden: ", hidden)