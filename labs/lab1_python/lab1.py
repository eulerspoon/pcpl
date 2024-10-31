import sys
import math

def get_coeff(coeff_name):
    while True:
        s = input(f"Введите коэффициент {coeff_name}: ")
        try: 
            return float(s)
        except:
            print("Введён неверный коэффициент!")

def no_roots(): print("Действительных корней нет.")

def print_roots(number, roots_set = set()):
    if number == 0:
        no_roots()
        return
    print(f"Количество корней: {number}")
    print("Корни:")
    for x in roots_set: print(x)

def solve_equation(a, b, c):
    roots = set()
    if a == 0:
        if b == 0:
            if c == 0:
                print("R")
                return
            print_roots(0)
            return
        roots.add(-c / b)
        print_roots(1, roots)
        return
    d = b * b - 4 * a * c
    if d == 0:
        new_root = (-b) / (2 * a)
        if new_root > 0:
            roots.add(math.sqrt(new_root))
            roots.add(-math.sqrt(new_root))
        elif new_root == 0:
            roots.add(0)
    elif d > 0:
        for i in range(2):
            new_root = (-b + (-1)**i * math.sqrt(d)) / (2 * a)
            if new_root > 0:
                roots.add(math.sqrt(new_root))
                roots.add(-math.sqrt(new_root))
            elif new_root == 0:
                roots.add(0)
    else:
        print_roots(0)
        return
    
    print_roots(len(roots), roots)
    
A = get_coeff('a')
B = get_coeff('b')
C = get_coeff('c')

solve_equation(A, B, C)















