import numpy as np

def p1(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    total = 0

    for bank in lines:
        digits = np.array(list(bank), dtype=np.int8)
        n = len(digits)

        suffix_max = np.maximum.accumulate(digits[::-1])[::-1]

        best_for_bank = 0

        for i in range(n - 1):
            tens = int(digits[i])
            ones = int(suffix_max[i + 1])
            val = tens * 10 + ones
            if val > best_for_bank:
                best_for_bank = val

        total += best_for_bank

    return total


def p2(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    K = 12  
    total = 0

    for bank in lines:
        digits = [int(c) for c in bank]
        n = len(digits)

        to_remove = n - K

        stack = []

        for d in digits:
            while to_remove > 0 and stack and stack[-1] < d:
                stack.pop()
                to_remove -= 1
            stack.append(d)

        chosen = stack[:K]

        val = int("".join(str(x) for x in chosen))
        total += val

    return total


with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()    

part1 = p1(text)
print(part1)
part2 = p2(text)
print(part2)
