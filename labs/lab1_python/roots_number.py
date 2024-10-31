import math

def roots_number(a, b, c):
    roots = 0
    if a == 0:
        if b == 0:
            if c == 0:
                return False
            return 0
        return 2

    d = b * b - 4 * a * c
    if d < 0: return 0
    if d == 0:
        if -b / a > 0: return 2
        elif -b / a == 0: return 1
        return 0
    for i in range(2):
        roots += 2 * (((-b) + (-1)**i * math.sqrt(d)) / (2 * a) > 0)
    return roots
