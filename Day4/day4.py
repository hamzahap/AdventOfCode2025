import numpy as np

def p1(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    grid = np.array([[1 if ch == '@' else 0 for ch in row] for row in lines], dtype=np.int8)
    H, W = grid.shape

    pad = np.pad(grid, pad_width=1, mode='constant', constant_values=0)

    up_left     = pad[0:H,  0:W  ]
    up          = pad[0:H,  1:W+1]
    up_right    = pad[0:H,  2:W+2]
    left        = pad[1:H+1,0:W  ]
    right       = pad[1:H+1,2:W+2]
    down_left   = pad[2:H+2,0:W  ]
    down        = pad[2:H+2,1:W+1]
    down_right  = pad[2:H+2,2:W+2]

    neighbor_count = (up_left + up + up_right + left + right + down_left + down + down_right)

    accessible_mask = (grid == 1) & (neighbor_count < 4)

    return int(accessible_mask.sum())

def p2(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    grid = np.array([[1 if ch == '@' else 0 for ch in row] for row in lines], dtype=np.int8)
    H, W = grid.shape

    total_removed = 0

    while True:
        pad = np.pad(grid, pad_width=1, mode='constant', constant_values=0)

        up_left     = pad[0:H,  0:W  ]
        up          = pad[0:H,  1:W+1]
        up_right    = pad[0:H,  2:W+2]
        left        = pad[1:H+1,0:W  ]
        right       = pad[1:H+1,2:W+2]
        down_left   = pad[2:H+2,0:W  ]
        down        = pad[2:H+2,1:W+1]
        down_right  = pad[2:H+2,2:W+2]

        neighbor_count = (up_left + up + up_right + left + right + down_left + down + down_right)

        removable = (grid == 1) & (neighbor_count < 4)
        removed_this_round = int(removable.sum())

        if removed_this_round == 0:
            break

        total_removed += removed_this_round
        grid[removable] = 0 

    return total_removed

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()    

part1 = p1(text)
print(part1)
part2 = p2(text)
print(part2)
