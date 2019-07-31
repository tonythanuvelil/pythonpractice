# Star tree
height = eval(input("Enter height of tree: "))
for row in range(height):
    for count in range(height - row):
        print(end=" ")
    for count in range(2*row+1):
            print(end="*")
    print()

# Box
print("Enter the size of the box:")
n = eval(input())
for i in range(n):
    for j in range(n):
        print(end="*")
    print()
