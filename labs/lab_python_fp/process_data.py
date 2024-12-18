import json
import sys
from print_result import print_result
from cm_timer import cm_timer_1
from unique import Unique
import random
from gen_random import gen_random

path = "data_light.json"

with open(path) as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    return list(Unique(x['job-name'] for x in data))


@print_result
def f2(arg):
    return list(filter(lambda x: x[:11].lower() == 'программист', arg))


@print_result
def f3(arg):
    return [x + 'с опытом Python' for x in arg]


@print_result
def f4(arg):
    s = f', зарплата {random.randint(100_000, 200_000)} руб.'
    return [x + f', зарплата {random.randint(100_000, 200_000)} руб.' for x in arg]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))