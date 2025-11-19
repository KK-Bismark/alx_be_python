# A python program to draw a simple text-based pattern


size = int(input("Enter the size of the pattern: "))
number = 0

while number < size:
    for index in range(0, size):
        print("*", end="")
    number += 1
    print()
