# Objects

x = 2
print(dir(x))
print(x.__add__(5))
print(int.__add__(4, 7))

s = 'Hello'
print(dir(s))
print(s.__add__(' Tony!'))

word1 = 'Wow'
word2 = 'Wow'
print('\nEquality:', word1 == word2, ' Alias:', word1 is word2)

name = input("\nPlease enter your name: ")
print("Hello " + name.upper() + ", how are you?\n")

word = name
print(word.rjust(10, "*"))
