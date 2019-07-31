# Lists or arrays for that matter

myList = [1, 2, 3, 4, 5]
for i in range(0, 5):
    print(myList[i])
# Your list can be this.
collection = [24.2, 4, 'word', eval, 19, -0.03, 'end']
print(collection)
print(collection[2])

# Or this, or anything you want.
col = [23, [9.3, 11.2, 99.0], [23], [], 4, [0, 0]]
print(col)
print(col[1])

# You know just some cool list stuff!
tony = []
print("\nEnter the elements to the list:")
for i in range(4):
    a = eval(input())
    tony += [a]
print(tony)
print("The first element is:", tony[0])
nn = False
for i in range(4):
    if type(tony[i]) == str:
        print("There is a string in the list:", tony[i])
        nn = True
if not nn:
    print("There is no string in the list.")
print("The second to last element is:", tony[-2])
print("Just the first 3 elements:", tony[0:3])

new = [i for i in range(1, 5)]
print("\nHere is another list:", new)
