import math

def calculate_x_recursive(n, current=0):
    if n == 0:
        return current
    return calculate_x_recursive(n - 1, math.sqrt(3 + current))
print(calculate_x_recursive(1))
print(calculate_x_recursive(2))
print(calculate_x_recursive(3))