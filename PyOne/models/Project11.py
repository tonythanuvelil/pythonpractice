# List Processing

# Sorting an integer array

myList = []
print("Enter the length of the integer list:")
n = eval(input())
print("Enter the elements of the list:")
for i in range(n):
    a = eval(input())
    myList += [a]
print("Before sorting:\n", myList)
for i in range(n):
    for j in range(n - 1):
        if myList[i] < myList[j]:
            temp = myList[i]
            myList[i] = myList[j]
            myList[j] = temp
print("After sorting:\n", myList)
