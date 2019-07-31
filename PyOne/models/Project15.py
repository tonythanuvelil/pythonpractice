# File management
print("tony.txt is open. Write something to the file:")
content = str(input())
f = open('tony.txt', 'w')
f.write(content)
f.close()
f = open('tony.txt', 'r')
print(f.read())
f.close()
for i in range(10, 0, -1):
    print(i)
