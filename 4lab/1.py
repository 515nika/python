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
