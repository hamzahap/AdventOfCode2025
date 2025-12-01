import numpy as np

def p1(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    
    dirs_char = np.array([line[0] for line in lines])
    dists = np.array([int(line[1:]) for line in lines])
    dir = np.where(dirs_char == 'R', 1, -1)
    steps = dir * dists  
    
    positions = (50 + np.cumsum(steps)) % 100 
    
    return (positions == 0).sum()


def p2(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    
    dirs_char = np.array([line[0] for line in lines])
    dists = np.array([int(line[1:]) for line in lines])
    dir = np.where(dirs_char == 'R', 1, -1)  
    steps = dir * dists                                        

    positions = (50 + np.cumsum(steps)) % 100   

    pos_before = np.empty_like(positions)
    pos_before[0] = 50
    pos_before[1:] = positions[:-1]

    p = pos_before
    s = dir
    n = dists

    r = (-s * p) % 100            
    k0 = r.copy()
    k0[k0 == 0] = 100                

    hit = n >= k0           
    counts = np.zeros_like(n)
    idx = np.where(hit)[0]
    counts[idx] = 1 + (n[idx] - k0[idx]) / 100

    return counts.sum()

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()    

part1 = p1(text)
print(part1)
part2 = p2(text)
print(part2)
