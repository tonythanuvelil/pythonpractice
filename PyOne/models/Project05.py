# Factorial
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print('Enter a value:')
n = eval(input())
print("The factorial is:", fact(n))
