import numpy as np

def p1(text):
    lines = [line.rstrip("\n") for line in text.splitlines() if line.strip()]
    if not lines:
        return 0

    H = len(lines)
    W = max(len(line) for line in lines)

    padded = [line.ljust(W) for line in lines]
    grid = np.array([list(row) for row in padded], dtype="<U1") 

    is_space = (grid == " ")
    sep_cols = is_space.all(axis=0)       
    content_cols = ~sep_cols            

    padded_content = np.concatenate(([False], content_cols, [False]))
    diff = np.diff(padded_content.astype(np.int8))

    starts = np.where(diff == 1)[0]       
    ends   = np.where(diff == -1)[0] - 1   

    total = 0

    for cs, ce in zip(starts, ends):
        block = grid[:, cs:ce+1]         
        op_row = block[-1, :]
        op_mask = (op_row == "+") | (op_row == "*")
        op_chars = op_row[op_mask]

        if op_chars.size == 0:
            continue 

        op = op_chars[0]

        nums = []
        for r in range(H - 1):
            row_chunk = block[r, :]                  
            s = "".join(row_chunk).strip()
            if s:
                nums.append(int(s))

        if not nums:
            continue

        if op == "+":
            val = sum(nums)
        else:
            prod = 1
            for x in nums:
                prod *= x
            val = prod

        total += val

    return total

def p2(text):
    lines = [line.rstrip("\n") for line in text.splitlines() if line.strip()]
    if not lines:
        return 0

    H = len(lines)
    W = max(len(line) for line in lines)

    padded = [line.ljust(W) for line in lines]
    grid = np.array([list(row) for row in padded], dtype="<U1") 

    is_space = (grid == " ")
    sep_cols = is_space.all(axis=0)   
    content_cols = ~sep_cols          

    padded_content = np.concatenate(([False], content_cols, [False]))
    diff = np.diff(padded_content.astype(np.int8))
    starts = np.where(diff == 1)[0]         
    ends   = np.where(diff == -1)[0] - 1  

    total = 0

    for cs, ce in zip(starts, ends):
        block = grid[:, cs:ce+1]     

        op_row = block[-1, :]
        op_mask = (op_row == "+") | (op_row == "*")
        op_chars = op_row[op_mask]
        if op_chars.size == 0:
            continue
        op = op_chars[0]

        nums = []

        for j in range(block.shape[1]):
            col = block[:-1, j]  
            is_digit = (col >= "0") & (col <= "9")
            digit_chars = col[is_digit]

            if digit_chars.size == 0:
                continue

            s = "".join(digit_chars.tolist())
            nums.append(int(s))

        if not nums:
            continue

        if op == "+":
            val = sum(nums)
        else:
            prod = 1
            for x in nums:
                prod *= x
            val = prod

        total += val

    return total

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()    

part1 = p1(text)
print(part1)
part2 = p2(text)
print(part2)
