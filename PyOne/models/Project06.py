# Fibonacci
def fib(f):
    if f <= 1:
        return f
    else:
        return fib(f - 1) + fib(f - 2)


print('Enter the number of terms:')
x = eval(input())
for i in range(x):
    print(fib(i), end=' ')

# Without recursion


print("\nEnter a value:")
n = eval(input())
a = 0
b = 1
fib = 0
if n <= 1:
    if n == 0:
        print("Invalid!")
    else:
        print(n - 1)
else:
    for i in range(n):
        fib = a + b
        a = b
        b = fib
        fib = fib - a
        print(fib, end=' ')
