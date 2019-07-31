# List Processing
# Linear Search

myList = []
print("Enter the length of the integer list:")
n = eval(input())
print("Enter the elements of the list:")
for i in range(n):
    a = eval(input())
    myList += [a]
print("The list is:", myList)
print("Enter the element you want to search:")
s = eval(input())


def search():
    for i in range(n):
        if myList[i] == s:
            return i


print("The element {0} found at: {1}".format(s, search() + 1))

# Reversing the list

revList = []
for i in range(n - 1, -1, -1):
    x = myList[i]
    revList += [x]
print("The reversed list is:", revList)
