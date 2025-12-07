import numpy as np

def p1(text):
    blocks = text.strip().split("\n\n")
    ranges_block = blocks[0].strip().splitlines()
    ids_block = blocks[1].strip().splitlines()

    ranges = []
    for line in ranges_block:
        line = line.strip()
        if not line:
            continue
        start_str, end_str = line.split("-")
        start = int(start_str)
        end = int(end_str)
        ranges.append((start, end))

    ranges.sort()

    merged = []
    cur_start, cur_end = ranges[0]
    for s, e in ranges[1:]:
        if s <= cur_end:  
            if e > cur_end:
                cur_end = e
        else:           
            merged.append((cur_start, cur_end))
            cur_start, cur_end = s, e
    merged.append((cur_start, cur_end))

    starts = np.array([r[0] for r in merged], dtype=np.int64)
    ends   = np.array([r[1] for r in merged], dtype=np.int64)

    ids = np.array([int(line.strip()) for line in ids_block if line.strip()], dtype=np.int64)

    idx = np.searchsorted(starts, ids, side="right") - 1
    fresh_mask = (idx >= 0) & (ids <= ends[idx])

    return int(fresh_mask.sum())

def p2(text):
    blocks = text.strip().split("\n\n")
    ranges_block = blocks[0].strip().splitlines()

    starts_list = []
    ends_list = []

    for line in ranges_block:
        line = line.strip()
        if not line:
            continue
        lo_str, hi_str = line.split("-")
        starts_list.append(int(lo_str))
        ends_list.append(int(hi_str))

    if not starts_list:
        return 0

    starts = np.array(starts_list, dtype=np.int64)
    ends   = np.array(ends_list,   dtype=np.int64)

    order = np.argsort(starts)
    starts = starts[order]
    ends   = ends[order]

    max_end_so_far = np.maximum.accumulate(ends[:-1])
    boundary_mask = starts[1:] > max_end_so_far   

    segment_starts_idx = np.concatenate((np.array([0], dtype=np.int64), np.nonzero(boundary_mask)[0] + 1))

    merged_starts = starts[segment_starts_idx]
    merged_ends   = np.maximum.reduceat(ends, segment_starts_idx)
    lengths = merged_ends - merged_starts + 1

    return int(lengths.sum())

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()    

part1 = p1(text)
print(part1)
part2 = p2(text)
print(part2)
