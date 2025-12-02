import numpy as np

def p1(text):
    line = text.strip().replace("\n", "")  
    parts = [p for p in line.split(",") if p]

    ranges = []
    for p in parts:
        start, end = p.split("-")
        s = int(start)
        e = int(end)
        ranges.append((s, e))

    ranges.sort()
    starts = np.array([r[0] for r in ranges])
    ends   = np.array([r[1] for r in ranges])

    global_min = int(starts.min())
    global_max = int(ends.max())

    candidates = []

    max_len = len(str(global_max))

    for length in range(2, max_len + 1, 2): 
        half = length // 2

        start_left = 10 ** (half - 1)
        end_left = 10 ** half

        for left in range(start_left, end_left):
            s = str(left)
            n = int(s + s) 

            if n > global_max:
                break
            if n >= global_min:
                candidates.append(n)

    if not candidates:
        return 0

    ids = np.array(candidates)
    idx = np.searchsorted(starts, ids, side="right") - 1
    mask = (idx >= 0) & (ids <= ends[idx])

    return int(ids[mask].sum())

def p2(text):
    line = text.strip().replace("\n", "")  
    parts = [p for p in line.split(",") if p]

    ranges = []
    for p in parts:
        start, end = p.split("-")
        s = int(start)
        e = int(end)
        ranges.append((s, e))

    ranges.sort()
    starts = np.array([r[0] for r in ranges])
    ends   = np.array([r[1] for r in ranges])

    global_min = int(starts.min())
    global_max = int(ends.max())

    candidates = set()

    max_len = len(str(global_max))

    for total_len in range(2, max_len + 1):
        for block_len in range(1, total_len // 2 + 1):
            if total_len % block_len != 0:
                continue

            repeat_count = total_len // block_len
            if repeat_count < 2:
                continue

            start_left = 10 ** (block_len - 1)
            end_left   = 10 ** block_len

            for left in range(start_left, end_left):
                s = str(left)
                n = int(s * repeat_count)  

                if n > global_max:
                    break
                if n >= global_min:
                    candidates.add(n)

    if not candidates:
        return 0

    ids = np.array(sorted(candidates))
    idx = np.searchsorted(starts, ids, side="right") - 1
    mask = (idx >= 0) & (ids <= ends[idx])

    return int(ids[mask].sum())

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()    

part1 = p1(text)
print(part1)
part2 = p2(text)
print(part2)
