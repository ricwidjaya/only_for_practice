# Create Fibonacci numbers with generators

def fib(n):
    a = 0
    b = 1
    for i in range(n):
        yield a             # return original a
        temp = a            # create a temporary a as a original for ascending use
        a = b               # let new a be original b
        b = temp + b        # let new b be original b + original a

print(list(fib(20)))