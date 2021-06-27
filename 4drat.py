import math


def solve(a, b, c):
    d = b * b - 4 * a * c
    if d < 0:
        print("No sol")
    elif d == 0:
        x = -b / (2 * a)
        print("1 sol")
    elif d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        print(f"sol x1 = {str(x1)} "
              f"x2 = {str(x2)}")
    else:
        print("wrong!")


solve(1, 1, 1)
solve(1, 2, 1)
solve(1, 5, 6)
