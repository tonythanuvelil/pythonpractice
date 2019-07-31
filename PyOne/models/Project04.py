print("Try some conditional statements now!")
print("Enter a value:")
x = eval(input())
if x < 0:
    print("Invalid!")
elif x == 0:
    print("Zero")
elif x == 1:
    print("One")
elif x == 2:
    print("Two")
else:
    print("Enter a lesser value!")
print("Finished.\n")

y = 1
while y <= 5:
    print("I'm from a while loop!")
    y = y + 1

print()

for i in range(1, 100):
    print(i)
    i = i + 1

print("\nThe above was a for loop!")

print("\nHappy Coding!")


