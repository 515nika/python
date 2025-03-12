import math

def calculate_x(n):
    result = 0
    for _ in range(n):
        result = math.sqrt(3 + result)
    return result
print(calculate_x(1))
print(calculate_x(2))
print(calculate_x(3))