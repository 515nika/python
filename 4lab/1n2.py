def cache_decorator(func):
    cache = {}
    
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    
    return wrapper
@cache_decorator
def fibonacci_closure():
    a, b = 0, 1
    
    def fibonacci():
        nonlocal a, b
        result = a
        a, b = b, a + b
        return result
    
    return fibonacci

fib = fibonacci_closure()
for i in range(10):
    print(fib(), end=" ")