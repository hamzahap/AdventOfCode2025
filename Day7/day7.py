import numpy as np

def p1(text):
    lines = [line.rstrip("\n") for line in text.splitlines() if line.strip()]
    H = len(lines)
    W = max(len(line) for line in lines)
    
    padded = [line.ljust(W, '.') for line in lines]
    grid = np.array([list(row) for row in padded], dtype="<U1")  
    
    S_pos = np.argwhere(grid == "S")
    if S_pos.size == 0:
        return 0
    start_r, start_c = S_pos[0]
    
    curr = np.zeros(W, dtype=bool)
    curr[start_c] = True
    
    split_count = 0
    
    for r in range(start_r, H - 1):
        below = grid[r + 1, :]         
        active = curr              
        
        splitter_hits = active & (below == "^")
        split_count += int(splitter_hits.sum())
        
        nxt = np.zeros(W, dtype=bool)
        
        cont = active & (below == ".")
        nxt[cont] = True
        
        hit_cols = np.where(splitter_hits)[0]
        if hit_cols.size > 0:
            left_cols = hit_cols - 1
            right_cols = hit_cols + 1
            
            left_cols = left_cols[left_cols >= 0]
            right_cols = right_cols[right_cols < W]
            
            nxt[left_cols] = True
            nxt[right_cols] = True
        
        curr = nxt
        if not curr.any():
            break
    
    return split_count

def p2(text):
    lines = [line.rstrip("\n") for line in text.splitlines() if line.strip()]
    if not lines:
        return 0

    H = len(lines)
    W = max(len(line) for line in lines)

    padded = [line.ljust(W, '.') for line in lines]
    grid = np.array([list(row) for row in padded], dtype="<U1") 

    S_pos = np.argwhere(grid == "S")
    if S_pos.size == 0:
        return 0
    start_r, start_c = map(int, S_pos[0])

    grid[start_r, start_c] = "."

    dp = np.zeros((H, W), dtype=object)
    dp[start_r, start_c] = 1

    total_timelines = 0

    for r in range(start_r, H):
        row_counts = dp[r, :]
        active_cols = np.nonzero(row_counts)[0]

        for c in active_cols:
            k = row_counts[c]
            if k == 0:
                continue

            if r == H - 1:
                total_timelines += k
                continue

            cell_below = grid[r + 1, c]

            if cell_below == ".":  
                dp[r + 1, c] = dp[r + 1, c] + k
            elif cell_below == "^":  
                if c - 1 >= 0:
                    dp[r + 1, c - 1] = dp[r + 1, c - 1] + k
                else:
                    total_timelines += k

                if c + 1 < W:
                    dp[r + 1, c + 1] = dp[r + 1, c + 1] + k
                else:
                    total_timelines += k
            else:
                dp[r + 1, c] = dp[r + 1, c] + k

    return total_timelines

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()    

part1 = p1(text)
print(part1)
part2 = p2(text)
print(part2)
