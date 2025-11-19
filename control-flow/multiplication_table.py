# A python program that generates the multiplication table of a user's number


number = int(input("Enter a number to see its multiplication table: "))

for num in range(1, 11):
    result = number * num
    print(f"{number} * {num} = {result}")
