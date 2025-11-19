# A python program that uses match case to make a simple calculator.


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 > 0:
            result = num1 / num2
        else:
            result = "The first number is indivisible by 0."
    case _:
        print("You didn't select the right operation.")

if result == int() or result == float():
    print(f"The result is {result}")
else:
    print(result)
