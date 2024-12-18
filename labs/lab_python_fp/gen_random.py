5, 1, 3
import random

def gen_random(num_count, begin, end):
    assert num_count > 0
    for x in range(num_count): yield random.randint(begin, end)

for x in gen_random(5, 1, 3):
    print(x)
